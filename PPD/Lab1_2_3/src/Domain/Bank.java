package Domain;

import java.util.ArrayList;
import java.util.Random;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicReference;

public class Bank {
    private final ArrayList<Account> accounts = new ArrayList<>();
    private AtomicInteger logId = new AtomicInteger(1);

    public Bank(int noAccounts){
        for (int i = 1; i < noAccounts; ++i){
            int startAmount = (int) (Math.random() * 1000);
            Account newAccount = new Account(i, startAmount);
            accounts.add(newAccount);
        }
    }

    public void checkConsistency(){
        this.accounts.forEach(account -> {
            account.lockAccount();
            AtomicInteger transferredAmount = new AtomicInteger(0);
            account.getLogs().forEach(log -> {
                if(log.from == account.getId()){
                    transferredAmount.addAndGet(-log.amount);
                } else {
                    transferredAmount.addAndGet(log.amount);
                }
            });
            assert account.getInitialBalance() + transferredAmount.get() == account.getBalance() : "Inconsistency detected in account" + account.getId();
            account.unlockAccount();
        });
        System.out.println("-------------------------> Checked consistency <-------------------------");
    }

    public void makeTransaction(int from, int to, int amount){
        Log log = new Log(logId.getAndIncrement(), from, to, amount);
        accounts.get(from).transfer(amount, log);
        accounts.get(to).receive(amount, log);
        System.out.println("From: " + from + " To: " + to + " Amount: " + amount + '\n');
    }

}
