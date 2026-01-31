import Threads.ConsumerThread;
import Threads.DataQueue;
import Threads.ProducerThread;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        List<Integer> vector1 = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));
        List<Integer> vector2 = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));

        DataQueue dataQueue = new DataQueue(2);

        // creating the Producer thread initialize with the 2 vectors and the queue
        ProducerThread producerThread = new ProducerThread(dataQueue, vector1, vector2);
        ConsumerThread consumerThread = new ConsumerThread(dataQueue, vector1.size());


        producerThread.start();
        consumerThread.start();
    }
}