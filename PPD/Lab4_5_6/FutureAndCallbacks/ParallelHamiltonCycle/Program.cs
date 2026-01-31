using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Threading;

class Program
{
    static int vertices;
    static List<int>[] adjList;
    static List<int> foundCycle = null;
    static readonly object lockObj = new object();

    // Graph initialization
    static void InitializeGraph(int v)
    {
        vertices = v;
        adjList = new List<int>[v];
        for (int i = 0; i < v; i++)
        {
            adjList[i] = new List<int>();
        }
    }

    // Add edge to the graph
    static void AddEdge(int u, int v)
    {
        adjList[u].Add(v);
    }

    // Check if the current path is a Hamiltonian cycle
    static bool IsHamiltonianCycle(List<int> path)
    {
        return path.Count == vertices && adjList[path[path.Count - 1]].Contains(path[0]);
    }

    // Parallel Hamiltonian cycle search
    static void ParallelHamiltonian(int current, bool[] visited, List<int> path)
    {
        // Stop if a cycle has been found
        lock (lockObj)
        {
            if (foundCycle != null)
                return;
        }

        // Add the current vertex to the path
        path.Add(current);
        visited[current] = true;

        // Check if the path forms a Hamiltonian cycle
        if (IsHamiltonianCycle(path))
        {
            lock (lockObj)
            {
                foundCycle = new List<int>(path);
            }
            return;
        }

        // Explore neighbors
        List<Thread> threads = new List<Thread>();
        foreach (var neighbor in adjList[current])
        {
            if (!visited[neighbor])
            {
                var neighborVisited = (bool[])visited.Clone();
                var neighborPath = new List<int>(path);

                Thread thread = new Thread(() => ParallelHamiltonian(neighbor, neighborVisited, neighborPath));
                threads.Add(thread);
                thread.Start();
            }
        }

        // Join threads
        foreach (var thread in threads)
        {
            thread.Join();
        }

        // Backtrack
        path.RemoveAt(path.Count - 1);
        visited[current] = false;
    }

    // Driver function to find Hamiltonian cycle
    static void FindHamiltonianCycle(int startVertex)
    {
        foundCycle = null; // Reset the result

        bool[] visited = new bool[vertices];
        List<int> path = new List<int>();

        Stopwatch stopwatch = new Stopwatch();
        stopwatch.Start();

        ParallelHamiltonian(startVertex, visited, path);

        stopwatch.Stop();

        if (foundCycle != null)
        {
            Console.WriteLine("Hamiltonian Cycle Found: " + string.Join(" -> ", foundCycle) + " -> " + foundCycle[0]);
        }
        else
        {
            Console.WriteLine("No Hamiltonian Cycle Found.");
        }

        Console.WriteLine($"Time taken: {stopwatch.ElapsedMilliseconds} ms");
    }

    static void Main(string[] args)
    {
        // Example graph setup
        InitializeGraph(5);
        AddEdge(0, 1);
        AddEdge(1, 2);
        AddEdge(2, 3);
        AddEdge(3, 0);
        AddEdge(3, 4);
        AddEdge(4, 0);

        Console.WriteLine("Searching for Hamiltonian Cycle...");
        FindHamiltonianCycle(0);
    }
}
