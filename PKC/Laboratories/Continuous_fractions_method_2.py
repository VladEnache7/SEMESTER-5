import math

def factorize(number):
    """Factorizes a number into its prime factors."""
    if number == 0:
        return [0]
    if number < 0:
        factors = [-1]
        number = -number
    else:
        factors = []

    # Trial division for small primes
    for i in range(2, int(math.sqrt(number)) + 1):
        while number % i == 0:
            factors.append(i)
            number //= i
    if number > 1:  # Remaining number is a prime
        factors.append(number)
    return factors

def calculate_values(number, iterations=8, base_initial=1):
    coefficients = []
    values_b = []
    fractions = []
    squared_b = []
    factorizations = []

    # Calculate initial values
    coefficients.append(int(math.sqrt(number)))
    values_b.append(coefficients[0])
    fractions.append(math.sqrt(number) - coefficients[0])

    # Calculate initial squared value
    squared_b_0 = (values_b[0] ** 2) % number

    if squared_b_0 > number / 2:
        squared_b_0 = - (number - squared_b_0)
    squared_b.append(squared_b_0)
    factorizations.append(factorize(squared_b_0))

    # Iterative computation
    for iteration in range(1, iterations):
        coefficients.append(int(1 / fractions[iteration - 1]) % number)
        fractions.append((1 / fractions[iteration - 1]) - coefficients[iteration] % number)

        if iteration == 1:
            values_b.append((coefficients[iteration] * values_b[iteration - 1] + base_initial) % number)
        else:
            values_b.append((coefficients[iteration] * values_b[iteration - 1] + values_b[iteration - 2]) % number)

        squared_b_i = (values_b[iteration] ** 2) % number
        if squared_b_i > number / 2:
            squared_b_i = - (number - squared_b_i)

        squared_b.append(squared_b_i)
        factorizations.append(factorize(squared_b_i))

    # Return results as a dictionary
    return {
        "coefficients": coefficients,
        "values_b": values_b,
        "fractions": fractions,
        "squared_b": squared_b,
        "factorizations": factorizations,
    }


if __name__ == "__main__":
    # Example usage
    result = calculate_values(7181)
    print("Coefficients: ", result["coefficients"])
    print("Values B: ", result["values_b"])
    print("Fractions: ", result["fractions"])
    print("Squared B: ", result["squared_b"])
    print("Factorizations: ", result["factorizations"])
