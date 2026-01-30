from __future__ import annotations

from typing import Callable


def gcd(a: int, b: int):
    """
    Computes the greatest common divisor (GCD) of two integers using the
    Euclidean algorithm. If b is 0, the GCD is a; otherwise, it recursively
    computes gcd(b, a % b).

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The GCD of a and b.
    """
    if b == 0:
        return a
    return gcd(b, a % b)


def pollardAlg(n: int, X0: int, func) -> tuple[int, float]:
    """
    Implements Pollard's Rho algorithm for integer factorization. This function
    attempts to find a non-trivial factor of the integer n by generating a
    sequence of values and checking for cycles. When a cycle is detected,
    it calculates the GCD of the cycle's difference with n, which may yield a factor.

    Parameters:
    n (int): The integer to factorize.
    X0 (int): The initial value in the sequence.
    func (Callable[[int], int]): A function used to generate the next value
                                  in the sequence.

    Returns:
    tuple[int, float]: A tuple containing a non-trivial factor of n and the
                       result of dividing n by this factor.
    """
    idx = 1  # Initialize the index for the sequence.
    Xs = [X0]  # Start the sequence with the initial value X0.

    # Loop indefinitely until a non-trivial divisor of n is found.
    while True:
        # Extend the sequence list until it has at least 2*idx elements.
        while len(Xs) - 1 < 2 * idx:
            Xs.append(func(Xs[-1]))  # Append the next value in the sequence.

        # Calculate the difference between the two sequence values at 2*idx and idx.
        difference = abs(Xs[2 * idx] - Xs[idx])

        # Compute the GCD of the difference and n.
        divisor = gcd(difference, n)

        # Check if the GCD is a non-trivial factor.
        if divisor not in (1, n):
            print('Idx', 2 * idx)
            print(f"Xs: {Xs[:len(Xs)//2]}")
            print("Difference: ", difference, "Divisor: ", divisor)
            return divisor, n / divisor  # Return the divisor and its complement factor.

        if divisor > n:
            return -1, -1

        idx += 1  # Increment the index and continue.


def build_polynomial(coefficients: list[int], n: int) -> Callable[[int], int]:
    """
    Creates a polynomial function based on the provided list of coefficients.
    Each coefficient corresponds to a term in the polynomial, where the index
    of the coefficient in the list represents the power of x.

    Parameters:
    coefficients (List[int]): A list of integer coefficients where the i-th element
                              is the coefficient for the x^i term. For example,
                              [1, 0, 1] represents the polynomial 1 + x^2.

    Returns:
    Callable[[int], int]: A function that calculates the polynomial's value for a given x.
                          When the returned function is called with an integer input x, it
                          computes the value of the polynomial by evaluating each term.

    Example:
    >>> poly_fn = build_polynomial([1, 0, 1])  # Represents the polynomial 1 + x^2
    >>> poly_fn(2)
    5  # since 1 + 2^2 = 5
    """

    def polynomial(x: int) -> int:
        """
        Computes the polynomial value for the given x.

        Parameters:
        x (int): The integer input to evaluate the polynomial at.

        Returns:
        int: The computed value of the polynomial for input x.
        """
        return sum(x ** i * c for i, c in enumerate(coefficients)) % n

    return polynomial


# Example usage
if __name__ == "__main__":
    N = 6283 # int(input("N = "))
    X0 = 2 # int(input("X0 = "))
    function = build_polynomial([1, 0, 1], N)   # [int(x) for x in input("Enter the function of the form (1, 0, 1) for 1 + X ** 2 = ").split(", ")])

    # Run Pollard's Rho algorithm and print the result.
    print(pollardAlg(N, X0, function))
