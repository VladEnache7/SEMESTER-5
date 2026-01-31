package Domain;

import java.util.ArrayList;
import java.util.concurrent.locks.ReentrantLock;

public class Account {
    public ReentrantLock mutex = new ReentrantLock();
    private final int id;
    private int balance;
    private final int initial_balance;
    private final ArrayList<Log> logs = new ArrayList<>();

    public Account(int id, int start_balance){
        this.id = id;
        this.initial_balance = this.balance = start_balance;
    }

    public int getBalance(){
        this.mutex.lock();
        try{
            return this.balance;
        } finally {
            this.mutex.unlock();
        }
    }

    public int getInitialBalance(){
        return this.initial_balance;
    }

    public void transfer(int amount, Log newRecord){
        this.lockAccount();
        try {
            this.balance -= amount;
            this.logs.add(newRecord);
        } finally {
            this.unlockAccount();
        }
    }

    public void receive(int amount, Log newRecord){
        this.lockAccount();
        try {
            this.balance += amount;
            this.logs.add(newRecord);
        } finally {
            this.unlockAccount();
        }
    }

    public ArrayList<Log> getLogs(){
        return this.logs;
    }

    public int getId(){
        return id;
    }

    public void lockAccount(){
        this.mutex.lock();
    }

    public void unlockAccount(){
        this.mutex.unlock();
    }
}
