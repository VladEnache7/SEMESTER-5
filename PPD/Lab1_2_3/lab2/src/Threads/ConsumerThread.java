package Threads;

import java.util.List;

public class ConsumerThread extends Thread {
    private DataQueue dataQueue;
    private Integer size;
    private int result;

    public ConsumerThread(DataQueue dataQueue, Integer size){
        this.dataQueue = dataQueue;
        this.size = size;
    }

    @Override
    public void run(){

        for(int i = 0; i < size; ++i){
            try {
                int gotProduct = dataQueue.get();
                result += gotProduct;
                System.out.println("Consumer - current Result = " + result);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            };
        }
        System.out.println("Consumer - Final result = " + result);

    }

}
