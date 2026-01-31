package Threads;

import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class DataQueue {
    private Queue<Integer> queue = new LinkedList<>();
    private ReentrantLock mutex = new ReentrantLock();
    private Condition condVar = mutex.newCondition();
    private int CAPACITY;

    public DataQueue(int maxSize){
        this.CAPACITY = maxSize;
    }

    public void put(Integer product) throws InterruptedException {
        mutex.lock();

        while(queue.size() == this.CAPACITY){
            System.out.println(Thread.currentThread().getName() + "Waiting for the buffer to get free!");
            condVar.await(); // waiting to get signaled be the other thread
        }

        queue.add(product);
        condVar.signalAll();
        System.out.println("Signaling that the buffer has an element now!");
        mutex.unlock();
    }

    public Integer get() throws InterruptedException {
        mutex.lock();
        try {
        while(queue.isEmpty()){
            System.out.println(Thread.currentThread().getName() + "Waiting for the buffer to get elements!");
            condVar.await();
        }
        Integer product = queue.remove();
        if (product != null){
            condVar.signalAll();
            System.out.println("Signaling that the buffer has a free space now!");
        }
        return product;
        } finally {
            mutex.unlock();
        }
    }
}
