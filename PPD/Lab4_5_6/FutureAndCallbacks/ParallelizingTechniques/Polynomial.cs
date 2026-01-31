namespace ParallelizingTechniques;

public class Polynomial
{
    public int[] Coefficients { get; }

    public Polynomial(int[] coefficients)
    {
        Coefficients = coefficients;
    }

    public int Degree => Coefficients.Length - 1;

    public override string ToString()
    {
        return string.Join(" ", Coefficients);
    }
}