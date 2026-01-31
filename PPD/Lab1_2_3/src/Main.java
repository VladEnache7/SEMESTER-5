import Domain.Bank;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        int NO_THREADS = 10;
        int NO_ACCOUNTS = 10;
        int OPERATIONS_PER_THREAD = 100;
        ArrayList<Thread> threads = new ArrayList<>();
        Bank bank = new Bank(NO_ACCOUNTS);
        Runnable consistencyTask = bank::checkConsistency;

        Runnable operationsTask = () -> {
            for(int i = 0; i < OPERATIONS_PER_THREAD; ++i){
                int from = ThreadLocalRandom.current().nextInt(0, NO_ACCOUNTS - 1);
                int to;
                do {
                    to = ThreadLocalRandom.current().nextInt(0, NO_ACCOUNTS - 1);
                } while(from == to);
                int amount = ThreadLocalRandom.current().nextInt(100);
                if (from > to){
                    int temp = from;
                    from = to;
                    to = temp;
                }
                bank.makeTransaction(from, to, amount);
            }
        };
        for (int i = 0; i < NO_THREADS; ++i){
            Thread newThread = new Thread(operationsTask);
            threads.add(newThread);
            newThread.start();
        }
        for(int i = 0; i < 3; ++i){
            Thread.sleep(new Random().nextInt(100));
            new Thread(consistencyTask).start();
        }


        for(int i = 0; i < NO_THREADS; ++i){
            threads.get(i).join();
        }

        bank.checkConsistency();
    }
}