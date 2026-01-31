import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CyclicBarrier;

public class OneThread extends Thread {
    private final int matrix_size, num_threads;
    private int idx;
    private final CyclicBarrier barrierStart, barrierEnd;

    public OneThread(int matrix_size, int current_idx, int num_threads, CyclicBarrier barrierStart, CyclicBarrier barrierEnd){
        this.matrix_size = matrix_size;
        this.idx = current_idx;
        this.num_threads = num_threads;
        this.barrierStart = barrierStart;
        this.barrierEnd = barrierEnd;
    }

    public void compute_sum(int row_idx, int col_idx){
        for(int k = 0; k < matrix_size; ++k){
            Main.result[row_idx][col_idx] += Main.MatrixA[row_idx][k] + Main.MatrixB[k][col_idx];
        }
    }

    @Override
    public void run(){
        try {
            // Wait for all threads to be ready
            barrierStart.await();
        } catch (InterruptedException | BrokenBarrierException e) {
            e.printStackTrace();
        }

        while(idx < matrix_size * matrix_size){
            compute_sum(idx / matrix_size, idx % matrix_size);
//            System.out.println("R[" + idx / matrix_size + "][" + idx % matrix_size + "] = " + Main.result[idx / matrix_size][idx % matrix_size]);
            idx += num_threads;
        }

        try {
            // Wait for all threads to be ready
            barrierEnd.await();
        } catch (InterruptedException | BrokenBarrierException e) {
            e.printStackTrace();
        }
    }
    
    
}
