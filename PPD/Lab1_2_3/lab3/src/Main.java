import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CyclicBarrier;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;


public class Main {
    private static long startTime;
    private static final int MATRIX_SIZE = 9;
    private static final int THREADS_NO = 8;
    public static int[][] MatrixA = new int[MATRIX_SIZE][MATRIX_SIZE];
    public static int[][] MatrixB = new int[MATRIX_SIZE][MATRIX_SIZE];
    public static int[][] result = new int[MATRIX_SIZE][MATRIX_SIZE];
    private static final List<Thread> threads = new ArrayList<Thread>();
    private static final CyclicBarrier barrierStart = new CyclicBarrier(THREADS_NO, new Runnable() {
        @Override
        public void run() {
            startTime = System.nanoTime();
            System.out.println("All threads are ready. Starting computation...");
        }
    });
    private static final CyclicBarrier barrierEnd = new CyclicBarrier(THREADS_NO, new Runnable() {
        @Override
        public void run() {
            System.out.println("The execution took:   " + (System.nanoTime() - startTime) / 1_000_000 + "   milliseconds.");
        }
    });

    public static void main(String[] args) throws InterruptedException, BrokenBarrierException {
        for(int i = 0; i < MATRIX_SIZE; ++i){
            for(int j = 0; j < MATRIX_SIZE; ++j) {
                MatrixA[i][j] = 1;
                MatrixB[i][j] = 1;
            }
        }
        ExecutorService executor = Executors.newFixedThreadPool(THREADS_NO);

        // Starting the threads
        for(int thread_idx = 0; thread_idx < THREADS_NO; ++thread_idx){
            System.out.println("Thread " + thread_idx + " started.");
//            Thread newThread = new OneThread(MATRIX_SIZE, thread_idx, THREADS_NO, barrierStart, barrierEnd);
//            threads.add(newThread);
//            newThread.start();
            executor.submit(new OneThread(MATRIX_SIZE, thread_idx, THREADS_NO, barrierStart, barrierEnd));

        }

        // Joining the threads
//        for(int i = 0; i < THREADS_NO; ++i)
//            threads.get(i).join();

       for(int i = 0; i < MATRIX_SIZE; ++i) {
           for (int j = 0; j < MATRIX_SIZE; ++j)
               System.out.print(Integer.toString(result[i][j]) + " ");
           System.out.println();
       }

//       System.out.println("The execution took:   " + (System.nanoTime() - startTime) / 1_000_000 + "   milliseconds.");
     }
}