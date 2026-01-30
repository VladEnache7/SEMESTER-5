from __future__ import annotations
from time import perf_counter
from texttable import Texttable


def gcdEuclidRecursive(a: int, b: int):
    """
    Performs the Euclidean algorithm recursively to find the greatest common divisor of two numbers.
    :param a: First number
    :param b: Second number
    :return: The greatest common divisor of a and b
    """
    if b == 0:
        return a
    return gcdEuclidRecursive(b, a % b)


def gcdEuclidIterative(a: int, b: int):
    """
    Performs the Euclidean algorithm iteratively to find the greatest common divisor of two numbers.
    :param a: First number
    :param b: Second number
    :return: The greatest common divisor of a and b
    """
    while b != 0:
        copy_a = a
        a = b
        b = copy_a % b
    return a


def gcdSubtractionRecursive(a: int, b: int):
    """
    Performs the subtraction algorithm recursively to find the greatest common divisor of two numbers.
    :param a: First number
    :param b: Second number
    :return: The greatest common divisor of a and b
    """
    if not a or not b:
        return max(a, b)
    if a == b:
        return a
    if a > b:
        return gcdSubtractionRecursive(b, a - b)
    return gcdSubtractionRecursive(a, b - a)


def gcdSubtractionIterative(a: int, b: int):
    """
    Performs the subtraction algorithm iteratively to find the greatest common divisor of two numbers.
    :param a: First number
    :param b: Second number
    :return: The greatest common divisor of a and b
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def gcd(a: int, b: int):
    """
    Computes the greatest common divisor of two numbers using the Euclidean algorithm.
    :param a: First number
    :param b: Second number
    :return: The greatest common divisor of a and b
    """
    if a == 0 or b == 0:
        return max(a, b)
    divisor = min(a, b)
    while divisor > 0:
        if a % divisor == 0 and b % divisor == 0:
            return divisor
        divisor -= 1
    return 1


if __name__ == "__main__":
    table = Texttable()
    table.add_row(["Numbers", 'Euclid Recursive', 'Euclid Iterative', 'Subtraction Recursive', 'Subtraction Iterative', 'GCD'])

    samples = [
        (12, 0),
        (1000, 10),
        (233, 144),
        (4181, 2584),
        (10946, 6765),
        (46368, 28657),
        (514229, 317811),
        (832040, 514229),
        (14930352, 9227465),
        (39088169, 24157817),
    ]
    for sample in samples:
        start_perf_counter1 = perf_counter()
        result1 = gcdEuclidRecursive(sample[0], sample[1])
        running_perf_counter_1 = (perf_counter() - start_perf_counter1) * 1000000

        start_perf_counter = perf_counter()
        result2 = gcdEuclidIterative(sample[0], sample[1])
        running_perf_counter_2 = (perf_counter() - start_perf_counter) * 1000000

        start_perf_counter = perf_counter()
        result3 = gcdSubtractionRecursive(sample[0], sample[1])
        running_perf_counter_3 = (perf_counter() - start_perf_counter) * 1000000

        start_perf_counter = perf_counter()
        result4 = gcdSubtractionRecursive(sample[0], sample[1])
        running_perf_counter_4 = (perf_counter() - start_perf_counter) * 1000000

        start_perf_counter = perf_counter()
        result5 = gcd(sample[0], sample[1])
        running_perf_counter_5 = (perf_counter() - start_perf_counter) * 1000000

        print(result1, result2, result3, result4, result5)
        table.add_row([sample, running_perf_counter_1, running_perf_counter_2, running_perf_counter_3, running_perf_counter_4, running_perf_counter_5])

    print(table.draw())


