#include <mpi.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using std::vector;
using std::cout;
using std::endl;

// Polynomial operations
vector<int> add(const vector<int>& A, const vector<int>& B) {
    size_t maxSize = std::max(A.size(), B.size());
    vector<int> result(maxSize, 0);
    for (size_t i = 0; i < maxSize; ++i) {
        if (i < A.size()) result[i] += A[i];
        if (i < B.size()) result[i] += B[i];
    }
    return result;
}

vector<int> subtract(const vector<int>& A, const vector<int>& B) {
    size_t maxSize = std::max(A.size(), B.size());
    vector<int> result(maxSize, 0);
    for (size_t i = 0; i < maxSize; ++i) {
        if (i < A.size()) result[i] += A[i];
        if (i < B.size()) result[i] -= B[i];
    }
    return result;
}

vector<int> multiplyNaive(const vector<int>& A, const vector<int>& B) {
    vector<int> result(A.size() + B.size() - 1, 0);
    for (size_t i = 0; i < A.size(); ++i) {
        for (size_t j = 0; j < B.size(); ++j) {
            result[i + j] += A[i] * B[j];
        }
    }
    return result;
}

vector<int> multiplyKaratsuba(const vector<int>& A, const vector<int>& B) {
    size_t n = std::max(A.size(), B.size());
    if (n <= 2) return multiplyNaive(A, B);

    size_t half = n / 2;

    vector<int> A_low(A.begin(), A.begin() + std::min(half, A.size()));
    vector<int> A_high(A.begin() + std::min(half, A.size()), A.end());
    vector<int> B_low(B.begin(), B.begin() + std::min(half, B.size()));
    vector<int> B_high(B.begin() + std::min(half, B.size()), B.end());

    vector<int> Z0 = multiplyKaratsuba(A_low, B_low);
    vector<int> Z2 = multiplyKaratsuba(A_high, B_high);
    vector<int> Z1 = multiplyKaratsuba(add(A_low, A_high), add(B_low, B_high));

    Z1 = subtract(subtract(Z1, Z0), Z2);

    vector<int> result(2 * n - 1, 0);
    for (size_t i = 0; i < Z0.size(); ++i) result[i] += Z0[i];
    for (size_t i = 0; i < Z1.size(); ++i) result[i + half] += Z1[i];
    for (size_t i = 0; i < Z2.size(); ++i) result[i + 2 * half] += Z2[i];

    return result;
}

void mpiDistributeAndCompute(const vector<int>& A, const vector<int>& B, bool useKaratsuba, MPI_Comm comm) {
    int rank, size;
    MPI_Comm_rank(comm, &rank);
    MPI_Comm_size(comm, &size);

    if (rank == 0) {
        vector<int> result(A.size() + B.size() - 1, 0);
        for (int i = 1; i < size; ++i) {
            MPI_Send(A.data(), A.size(), MPI_INT, i, 0, comm);
            MPI_Send(B.data(), B.size(), MPI_INT, i, 1, comm);
        }

        for (int i = 1; i < size; ++i) {
            vector<int> partial(A.size() + B.size() - 1, 0);
            MPI_Recv(partial.data(), partial.size(), MPI_INT, i, 2, comm, MPI_STATUS_IGNORE);
            for (size_t j = 0; j < result.size(); ++j) result[j] += partial[j];
        }

        cout << "Resultant Polynomial: ";
        for (size_t i = 0; i < result.size(); ++i) {
            cout << result[i];
            if (i > 0) cout << "x^" << i;
            if (i < result.size() - 1) cout << " + ";
        }
        cout << endl;
    } else {
        vector<int> localA(A.size()), localB(B.size());
        MPI_Recv(localA.data(), A.size(), MPI_INT, 0, 0, comm, MPI_STATUS_IGNORE);
        MPI_Recv(localB.data(), B.size(), MPI_INT, 0, 1, comm, MPI_STATUS_IGNORE);

        vector<int> partial = useKaratsuba ? multiplyKaratsuba(localA, localB) : multiplyNaive(localA, localB);
        MPI_Send(partial.data(), partial.size(), MPI_INT, 0, 2, comm);
    }
}

int main(int argc, char* argv[]) {
    MPI_Init(&argc, &argv);

    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    vector<int> A = {1, 2, 3}; // A(x) = 1 + 2x + 3x^2
    vector<int> B = {3, 5, 6}; // B(x) = 4 + 5x + 6x^2

    if (rank == 0) cout << "Using Regular Multiplication:\n";
    mpiDistributeAndCompute(A, B, false, MPI_COMM_WORLD);

    if (rank == 0) cout << "Using Karatsuba Multiplication:\n";
    mpiDistributeAndCompute(A, B, true, MPI_COMM_WORLD);

    MPI_Finalize();
    return 0;
}
