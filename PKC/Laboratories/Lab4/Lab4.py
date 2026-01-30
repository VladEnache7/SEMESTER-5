import random
from sympy import isprime
import sympy

ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generate_key() -> [int, tuple[int, int]]:
    """Generates public and private keys for the Rabin Cryptosystem."""
    while True:
        p = random.getrandbits(256) | 3  # Small prime for example purposes
        q = random.getrandbits(256) | 3  # Ensuring p ≡ q ≡ 3 (mod 4)
        if isprime(p) and isprime(q) and p % 4 == 3 and q % 4 == 3:
            break

    n = p * q  # Public key
    return (n, (p, q))


def get_message():
    alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    message = input("Enter the message you want to encrypt: ")
    # Convert to binary and then to int
    message = ''.join(format(ord(char), '08b') for char in message)
    message = int(message, 2)
    return message


def encode_message(message: str, k: int) -> list[int]:
    """Encodes a message into blocks of length k."""

    message = message.upper().ljust((len(message) + k - 1) // k * k)  # Pad with spaces
    blocks = [message[i:i + k] for i in range(0, len(message), k)]
    return [sum((ALPHABET.index(ch) * (27 ** (k - j - 1))) for j, ch in enumerate(block)) for block in blocks]






def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Computes the extended Euclidean algorithm for two integers a and b."""
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - (a // b) * y


def decode_message(blocks: list[int], k: int) -> str:
    """Decodes blocks of integers into a message."""
    decoded = ""
    for block in blocks:
        temp = []
        for _ in range(k):
            temp.append(ALPHABET[block % 27])
            block //= 27
        decoded += "".join(reversed(temp))
    return decoded.strip()


def choose(possible_plaintexts: list[int]) -> int:
    """Chooses the correct plaintext from the list of possible plaintexts."""
    for pt in possible_plaintexts:
        binary = bin(pt)[2:]  # Convert to binary string and remove '0b' prefix
        if len(binary) % 8 == 0:  # Check if the length is a multiple of 8
            return pt
    return None



if __name__ == "__main__":
    public_key, private_key = generate_key()
    message = get_message()
    print(f"Message: {message}")
    ciphertext = encrypt(message, public_key)
    print(f"Ciphertext: {ciphertext}")
    possible_plaintexts = decrypt(ciphertext, private_key)
    for pt in possible_plaintexts:
        print(f"Possible plaintext: {pt}")
    decrypted_message = choose(possible_plaintexts)
    print(f"Decrypted message: {decrypted_message}")

    # assert message == decrypted_message, "Decryption failed!"


