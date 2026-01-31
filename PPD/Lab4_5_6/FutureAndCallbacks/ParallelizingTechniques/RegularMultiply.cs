namespace ParallelizingTechniques;

public class RegularMultiply
{
    public static Polynomial Compute(Polynomial p1, Polynomial p2)
    {
        int[] result = new int[p1.Degree + p2.Degree + 2];

        for (int i = 0; i <= p1.Degree; i++)
        {
            for (int j = 0; j <= p2.Degree; j++)
            {
                result[i + j] += p1.Coefficients[i] * p2.Coefficients[j];
            }
        }

        return new Polynomial(result);
    }    
} 
