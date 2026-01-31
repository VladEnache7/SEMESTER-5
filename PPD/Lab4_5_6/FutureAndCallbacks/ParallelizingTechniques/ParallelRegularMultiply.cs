namespace ParallelizingTechniques;

public class ParallelRegularMultiply
{
    public static Polynomial Compute(Polynomial p1, Polynomial p2)
    {
        int[] result = new int[p1.Degree + p2.Degree + 2];

        Parallel.For(0, p1.Degree + 1, i =>
        {
            for (int j = 0; j <= p2.Degree; j++)
            {
                Interlocked.Add(ref result[i + j], p1.Coefficients[i] * p2.Coefficients[j]);
            }
        });

        return new Polynomial(result);
    }    
}