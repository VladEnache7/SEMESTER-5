
# ⚡ Parallel and Distributed Programming

This course covers the theoretical and practical aspects of concurrent, parallel, and distributed computing. You will move from writing single-threaded applications to developing complex systems that leverage multi-core processors, clusters (MPI), and Graphics Processing Units (CUDA).

> **Note:** All official lecture slides, lab requirements, and detailed assignments can be found on the **[Professor's Website](https://www.cs.ubbcluj.ro/~rlupsa/edu/pdp/)**.

### 📅 Weekly Syllabus

The course explores different architectures and models of parallelism, from shared memory to distributed message passing.

| Week | 👨‍🏫 Lecture Content | 📝 Seminar & Lab Focus |
|:---:|:---|:---|
| **1** | **Intro:** Parallelism vs Concurrency, Levels of Parallelism | **S1/L1:** Threads vs Processes |
| **2** | **Architectures:** Pipeline, Vectorial, Grid, Clusters | **L2:** Concurrent Programming (Start) |
| **3** | **Basics:** Process/Thread Management | **L3:** Concurrent Programming (C++/Java/C#) |
| **4** | **Concurrency:** Race Conditions, Deadlocks, Mutexes, Semaphores | **L4:** Concurrent Programming (Continued) |
| **5** | **Models:** Implicit vs Explicit, Data Parallelism, Shared Memory | **L5:** Concurrent Programming (Finalize) |
| **6** | **Shared Memory:** Pthreads, C++ Threads, Java Threads, OpenMP | **S3/L6:** OpenMP |
| **7** | **Performance:** PRAM Model, Efficiency, Speedup, Scalability | **L7:** OpenMP (Continued) |
| **8** | **Patterns:** Master-Slave, Worker Pool, Pipeline, Divide & Conquer | **S4:** Parallel Design Patterns |
| **9** | **Message Passing:** MPI (Message Passing Interface) Introduction | **S5/L8:** MPI Basics |
| **10** | **Design Phases:** PCAM (Partition, Communication, Aggregation, Mapping) | **L9:** MPI Advanced |
| **11** | **Construction:** Binary Tree, Recursive Double-back techniques | **S6/L10:** MPI Optimization |
| **12** | **Data Parallelism:** Techniques and strategies | **S7/L11:** CUDA / OpenCL Start |
| **13** | **GPGPU:** General Processing on GPU (CUDA, OpenCL) | **L12:** CUDA / OpenCL Implementation |
| **14** | **Distributed Systems:** Distributed File Systems | **L13-14:** Final Project / CUDA |

---

### 💻 Laboratory & Practical Learning

The laboratory work is divided into specific technologies, requiring you to solve similar problems using different parallel paradigms to understand the trade-offs.

#### 🧪 Lab Phase 1: Native Threads & Concurrency
*   **Goal:** Master low-level thread management.
*   **Tech:** C++ `std::thread`, Java Threads, or C# Tasks.
*   **Concepts:** Handling race conditions, implementing barriers, producer-consumer problems, and avoiding deadlocks using Mutexes/Semaphores.

#### 🧪 Lab Phase 2: OpenMP (Shared Memory)
*   **Goal:** Use compiler directives to parallelize code easily.
*   **Tech:** C/C++ with OpenMP.
*   **Concepts:** Parallel `for` loops, scheduling (static vs dynamic), sections, and critical blocks.

#### 🧪 Lab Phase 3: MPI (Distributed Memory)
*   **Goal:** Write programs that run across multiple machines (nodes).
*   **Tech:** MPI (Message Passing Interface).
*   **Concepts:** `MPI_Send`, `MPI_Recv`, Collective communication (`Broadcast`, `Scatter`, `Gather`, `Reduce`), and non-blocking communication.

#### 🧪 Lab Phase 4: GPGPU (CUDA / OpenCL)
*   **Goal:** Offload massive parallel computations to the Video Card.
*   **Tech:** NVIDIA CUDA or OpenCL.
*   **Concepts:** Kernels, Thread Blocks, Grids, Shared vs Global Memory, and Memory Coalescing.

---

### 🧠 Competencies Acquired

**Technical Skills:**
*   **Performance Analysis:** Calculating Speedup ($S_p$) and Efficiency ($E_p$).
*   **Synchronization:** Correctly using locks, monitors, and barriers to prevent data corruption.
*   **Architecture Selection:** Knowing when to use a GPU vs. a CPU Cluster.
*   **Pattern Implementation:** Applying Master-Worker or Pipeline patterns to real algorithms (e.g., Matrix Multiplication, Convolution, Sorting).

---

### 🛠️ Resources & Tools

*   **Languages:** C++, Java, C#, C (for MPI/CUDA).
*   **Libraries:** OpenMP, MS-MPI / OpenMPI, CUDA Toolkit.
*   **Hardware:** Access to multi-core CPUs and NVIDIA GPUs (often provided via University labs for CUDA tasks).
