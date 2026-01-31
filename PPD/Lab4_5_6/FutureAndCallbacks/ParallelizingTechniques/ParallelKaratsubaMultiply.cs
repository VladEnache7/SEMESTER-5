namespace ParallelizingTechniques;

public class ParallelKaratsubaMultiply
{

    public static Polynomial Compute(Polynomial p1, Polynomial p2)
    {
        if (p1.Degree < 2 || p2.Degree < 2)
        {
            return RegularMultiply.Compute(p1, p2);
        }

        int m = Math.Max(p1.Degree, p2.Degree) / 2;

        Polynomial low1 = new Polynomial(p1.Coefficients.Take(m).ToArray());
        Polynomial high1 = new Polynomial(p1.Coefficients.Skip(m).ToArray());
        Polynomial low2 = new Polynomial(p2.Coefficients.Take(m).ToArray());
        Polynomial high2 = new Polynomial(p2.Coefficients.Skip(m).ToArray());

        Polynomial z0 = null, z1 = null, z2 = null;

        Parallel.Invoke(
            () => z0 = ParallelKaratsubaMultiply.Compute(low1, low2),
            () => z1 = ParallelKaratsubaMultiply.Compute(Add(low1, high1), Add(low2, high2)),
            () => z2 = ParallelKaratsubaMultiply.Compute(high1, high2)
        );

        int[] result = new int[p1.Degree + p2.Degree + 2];

        for (int i = 0; i < z0.Coefficients.Length; i++)
            result[i] += z0.Coefficients[i];

        for (int i = 0; i < z1.Coefficients.Length; i++)
        {
            int z0Coeff = i < z0.Coefficients.Length ? z0.Coefficients[i] : 0;
            int z2Coeff = i < z2.Coefficients.Length ? z2.Coefficients[i] : 0;
            result[i + m] += z1.Coefficients[i] - z0Coeff - z2Coeff;
        }

        for (int i = 0; i < z2.Coefficients.Length; i++)
            result[i + 2 * m] += z2.Coefficients[i];

        return new Polynomial(result);
    }
    
    private static Polynomial Add(Polynomial p1, Polynomial p2)
    {
        int maxDegree = Math.Max(p1.Degree, p2.Degree);
        int[] result = new int[maxDegree + 1];

        for (int i = 0; i <= maxDegree; i++)
        {
            int coeff1 = i <= p1.Degree ? p1.Coefficients[i] : 0;
            int coeff2 = i <= p2.Degree ? p2.Coefficients[i] : 0;
            result[i] = coeff1 + coeff2;
        }

        return new Polynomial(result);
    }
}