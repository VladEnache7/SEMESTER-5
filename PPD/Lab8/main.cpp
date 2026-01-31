#include <mpi.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

// Utility functions
vector<int> addPolynomials(const vector<int>& A, const vector<int>& B) {
    int size = max(A.size(), B.size());
    vector<int> result(size, 0);
    for (int i = 0; i < size; i++) {
        if (i < A.size()) result[i] += A[i];
        if (i < B.size()) result[i] += B[i];
    }
    return result;
}

vector<int> subtractPolynomials(const vector<int>& A, const vector<int>& B) {
    int size = max(A.size(), B.size());
    vector<int> result(size, 0);
    for (int i = 0; i < size; i++) {
        if (i < A.size()) result[i] += A[i];
        if (i < B.size()) result[i] -= B[i];
    }
    return result;
}

// Regular O(n^2) polynomial multiplication
vector<int> regularMultiplication(const vector<int>& A, const vector<int>& B) {
    int n = A.size(), m = B.size();
    vector<int> result(n + m - 1, 0);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            result[i + j] += A[i] * B[j];
        }
    }
    return result;
}

// Karatsuba multiplication
vector<int> karatsubaMultiplication(const vector<int>& A, const vector<int>& B) {
    int n = max(A.size(), B.size());
    if (n <= 2) return regularMultiplication(A, B);

    int half = n / 2;

    vector<int> A_low(A.begin(), A.begin() + min((int)A.size(), half));
    vector<int> A_high(A.begin() + min((int)A.size(), half), A.end());
    vector<int> B_low(B.begin(), B.begin() + min((int)B.size(), half));
    vector<int> B_high(B.begin() + min((int)B.size(), half), B.end());

    vector<int> Z0 = karatsubaMultiplication(A_low, B_low);
    vector<int> Z2 = karatsubaMultiplication(A_high, B_high);
    vector<int> Z1 = karatsubaMultiplication(addPolynomials(A_low, A_high), addPolynomials(B_low, B_high));

    Z1 = subtractPolynomials(subtractPolynomials(Z1, Z0), Z2);

    vector<int> result(2 * n - 1, 0);
    for (int i = 0; i < Z0.size(); i++) result[i] += Z0[i];
    for (int i = 0; i < Z1.size(); i++) result[i + half] += Z1[i];
    for (int i = 0; i < Z2.size(); i++) result[i + 2 * half] += Z2[i];

    return result;
}

// Distribute tasks using MPI
void mpiPolynomialMultiplication(const vector<int>& A, const vector<int>& B, bool useKaratsuba, MPI_Comm comm) {
    int rank, size;
    MPI_Comm_rank(comm, &rank);
    MPI_Comm_size(comm, &size);


    if (rank == 0) {
        // Root process distributes work
        int n = A.size(), m = B.size();
        vector<int> result(n + m - 1, 0);

        for (int i = 1; i < size; i++) {


            MPI_Send(A.data(), A.size(), MPI_INT, i, 0, comm);
            MPI_Send(B.data(), B.size(), MPI_INT, i, 1, comm);
        }

        // Collect results
        for (int i = 1; i < size; i++) {
            vector<int> partialResult(n + m - 1);
            MPI_Recv(partialResult.data(), partialResult.size(), MPI_INT, i, 2, comm, MPI_STATUS_IGNORE);

            for (int j = 0; j < result.size(); j++) {
                result[j] += partialResult[j];
            }
        }

        // Display result
        cout << "Resultant Polynomial: ";
        for (size_t i = 0; i < result.size(); i++) {
            cout << result[i];
            if (i > 0) cout << "x^" << i;
            if (i < result.size() - 1) cout << " + ";
        }
        cout << endl;
    }
    else {
        // Worker processes receive data
        int n = A.size(), m = B.size();
        vector<int> localA(n), localB(m);

        MPI_Recv(localA.data(), n, MPI_INT, 0, 0, comm, MPI_STATUS_IGNORE);
        MPI_Recv(localB.data(), m, MPI_INT, 0, 1, comm, MPI_STATUS_IGNORE);

        vector<int> partialResult = useKaratsuba
                                    ? karatsubaMultiplication(localA, localB)
                                    : regularMultiplication(localA, localB);

        MPI_Send(partialResult.data(), partialResult.size(), MPI_INT, 0, 2, comm);
    }
}

int main(int argc, char* argv[]) {
    MPI_Init(&argc, &argv);

    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    // Example polynomials
    vector<int> A = { 1, 2, 3 }; // A(x) = 1 + 2x + 3x^2
    vector<int> B = { 4, 5, 6 }; // B(x) = 4 + 5x + 6x^2

    if (rank == 0) {
        cout << "Using Regular O(n^2) Algorithm:" << endl;
    }
    mpiPolynomialMultiplication(A, B, false, MPI_COMM_WORLD);

    if (rank == 0) {
        cout << "Using Karatsuba Algorithm:" << endl;
    }
    mpiPolynomialMultiplication(A, B, true, MPI_COMM_WORLD);

    MPI_Finalize();
    return 0;
}