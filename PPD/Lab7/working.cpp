#include <iostream>
#include <unordered_map>
#include <vector>
#include <thread>
#include <chrono>
#include <mpi.h>

// DSMVariable: Encapsulates shared memory variables
class DSMVariable {
private:
    int value;
    int id;
    std::vector<int> subscribers;

public:
    DSMVariable() : id(0), value(0), subscribers() {}

    DSMVariable(int id, int initialValue, const std::vector<int>& subs)
        : id(id), value(initialValue), subscribers(subs) {}

    int getId() const { return id; }

    int getValue() { return value; }

    void setValue(int newValue) { value = newValue; }

    const std::vector<int>& getSubscribers() const { return subscribers; }
};

class MPIHandler {
public:
    static void init(int argc, char** argv) {
        MPI_Init(&argc, &argv);
    }

    static void finalize() {
        MPI_Finalize();
    }

    static int getRank() {
        int rank;
        MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        return rank;
    }

    static int getSize() {
        int size;
        MPI_Comm_size(MPI_COMM_WORLD, &size);
        return size;
    }
};


// DSMManager: Manages DSM operations
class DSMManager {
private:
    std::unordered_map<int, DSMVariable> variables;
    int logicalClock;
    bool stopFlag;

public:
    DSMManager() : logicalClock(0), stopFlag(false) {}

    void addVariable(int id, int initialValue, const std::vector<int>& subscribers) {
        if (variables.count(id) == 0) {
            variables.emplace(id, DSMVariable(id, initialValue, subscribers));
        }
    }

    void writeVariable(int varId, int value) {
        if (variables.count(varId) == 0) return;

        logicalClock++;
        int message[3] = {varId, value, logicalClock}; // [variable_id, value, timestamp]

        DSMVariable& var = variables[varId];
        std::cout << "Writing variable " << varId << " to " << value << "\n";
        var.setValue(value);
        std::cout << "Variable " << varId << " updated to " << value << "\n";
        // Send the change to all subscribers
        for (int subscriber : var.getSubscribers()) {
            std::cout << "Sending update to process " << subscriber << "\n";
            MPI_Send(&message, 3, MPI_INT, subscriber, 0, MPI_COMM_WORLD);
        }
    }

    bool compareAndExchange(int varId, int expectedValue, int newValue) {
         std :: cout << "Attempting Compare-and-Exchange on variable " << varId
                    << " (expected: " << expectedValue << ", new value: " << newValue << ")\n";
        if (variables.count(varId) == 0) {
            std::cout << "Variable " << varId << " not found in DSM.\n";
            return false;
        }

        DSMVariable& var = variables[varId];
        if (var.getValue() == expectedValue) {
             std::cout << "Performing Compare-and-Exchange on variable " << varId << "\n";
            writeVariable(varId, newValue);
            return true;
        } else {
            std::cout << "Failed Compare-and-Exchange on variable " << varId
                      << " (expected value did not match).\n";
            std::cout << "Current value of variable " << varId << " is " << var.getValue() << "\n";
            std::cout << "Expected value was " << expectedValue << "\n";
        }
        return false;
    }

    void listenForUpdates(int rank) {
        int message[3]; // [variable_id, value, timestamp]
        MPI_Status status;

        while (true) {
            MPI_Recv(&message, 3, MPI_INT, MPI_ANY_SOURCE, 0, MPI_COMM_WORLD, &status);

            int varId = message[0];
            int newValue = message[1];
            int timestamp = message[2];

            // Check if it's a stop signal
            if (message[0] == -1) {
                std::cout << "Process " << rank << " received stop signal. Exiting.\n";
                break;
            }

            std::cout << "Process " << rank << " received update: Variable " << varId << " changed to " << newValue << " at timestamp " << timestamp << "\n";
            // Ensure all processes receive changes in the same order
            if (variables.count(varId)) {
                DSMVariable& var = variables[varId];
                var.setValue(newValue);
                std::cout << "Process " << rank << " updated: Variable " << varId << " changed to " << newValue << "\n";
            }
        }
    }

    void sendStopSignal() {
        int stopMessage[3] = {-1, 0, 0}; // Special stop signal with varId=-1
        int size = MPIHandler::getSize();
        for (int i = 1; i < size; ++i) {
            MPI_Send(&stopMessage, 3, MPI_INT, i, 0, MPI_COMM_WORLD); // Send stop signal to other processes
        }
    }

    void setStopFlag(bool flag) { stopFlag = flag; }

    bool getStopFlag() const { return stopFlag; }
};


// Main program
int main(int argc, char** argv) {
    MPIHandler::init(argc, argv);

    int rank = MPIHandler::getRank();
    int size = MPIHandler::getSize();

    std::cout << "Hello from process " << rank << " of " << size << "\n";

    DSMManager dsmManager;

    // Node 0 initializes variables and sends messages
    if (rank == 0) {
        dsmManager.addVariable(1, 0, {1, 2}); // Variable 1, initially 0, with subscribers 1 and 2

        std::cout << "Process 0 initialized variable 1 to 0\n";

        // Write a variable and send it to subscribers
        std::this_thread::sleep_for(std::chrono::seconds(1));  // Simulating delays for synchronization
        std::cout << "Process 0 writes variable 1 to 42\n";
        dsmManager.writeVariable(1, 42); // Process 0 sets variable 1 to 42

        std::this_thread::sleep_for(std::chrono::seconds(1));

        // Perform a Compare-and-Exchange operation
        std::cout << "Process 0 performs Compare-and-Exchange on variable 1\n";
        dsmManager.compareAndExchange(1, 42, 84); // Process 0 compares and changes variable 1 to 84

        // After operations, send stop signal
        dsmManager.sendStopSignal(); // Stop all other processes
    } else {
        // Other nodes listen for updates
        dsmManager.listenForUpdates(rank);
    }

    // Allow time for all processes to handle updates before finalizing MPI
    std::this_thread::sleep_for(std::chrono::seconds(5));

    MPIHandler::finalize();
    return 0;
}
