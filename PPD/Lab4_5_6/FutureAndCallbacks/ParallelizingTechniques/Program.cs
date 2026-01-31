namespace ParallelizingTechniques;

// call the main 
class Program
{
    public static void Main()
    {   
        int n = 1000;
        int[] coefficients = Enumerable.Range(1, n).ToArray();
        Polynomial p1 = new Polynomial(coefficients);
        Polynomial p2 = new Polynomial(coefficients.Reverse().ToArray());

        var start = DateTime.UtcNow;
        var result = RegularMultiply.Compute(p1, p2);
        var elapsed = DateTime.UtcNow - start;
        Console.WriteLine($"Regular Multiply: {elapsed.TotalMilliseconds} ms");

        start = DateTime.UtcNow;
        result = KaratsubaMultiply.Compute(p1, p2);
        elapsed = DateTime.UtcNow - start;
        Console.WriteLine($"Karatsuba Multiply: {elapsed.TotalMilliseconds} ms");

        start = DateTime.UtcNow;
        result = ParallelRegularMultiply.Compute(p1, p2);
        elapsed = DateTime.UtcNow - start;
        Console.WriteLine($"Parallel Regular Multiply: {elapsed.TotalMilliseconds} ms");

        start = DateTime.UtcNow;
        result = ParallelKaratsubaMultiply.Compute(p1, p2);
        elapsed = DateTime.UtcNow - start;
        Console.WriteLine($"Parallel Karatsuba Multiply: {elapsed.TotalMilliseconds} ms");
    }
}