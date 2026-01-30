def gcd(a, b):
    """Finds the greatest common divisor of a and b"""
    if a < b:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)

def is_prime(n: int) -> bool:
    """Checks if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def isCarmichaelNumber(number: int) -> bool:
    """Tests if the number is a carmichale number"""
    if is_prime(number):
        return False

    for d in range(2, number):
        if gcd(d, number) == 1 and pow(d, number, number) != d:
            return False

    return True


def getCarmichaelNumbers(upperBound:  int):
    return [carmichael for carmichael in range(560, upperBound) if isCarmichaelNumber(carmichael)]


if __name__ == "__main__":

    UPPER_BOUND = 10 ** 5
    print(getCarmichaelNumbers(UPPER_BOUND))
