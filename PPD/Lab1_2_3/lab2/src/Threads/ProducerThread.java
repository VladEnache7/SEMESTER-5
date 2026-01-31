package Threads;

import java.util.List;

public class ProducerThread extends Thread {
    private List<Integer> vector1, vector2;
    private DataQueue dataQueue;

    public ProducerThread(DataQueue dataQueue, List<Integer> vector1, List<Integer> vector2){
        if (vector1.size() != vector2.size()){
            throw new Error("Vectors should be of the same size");
        }
        this.dataQueue = dataQueue;
        this.vector1 = vector1;
        this.vector2 = vector2;
    }

    @Override
    public void run(){
        for(int i = 0; i < vector1.size(); ++i){
            Integer product = vector1.get(i) * vector2.get(i);
            try {
                dataQueue.put(product);
                System.out.println("Producer as placed an element.");
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            };
        }
    }

}
