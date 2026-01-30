import random
from sympy import isprime
from math import gcd

ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def generate_key() -> tuple[int, tuple[int, int]]:
    """Generates public and private keys for the Rabin Cryptosystem."""
    while True:
        p = random.getrandbits(64) | 3  # Small primes for demonstration
        q = random.getrandbits(64) | 3
        if isprime(p) and isprime(q) and p % 4 == 3 and q % 4 == 3:
            break

    n = p * q
    return n, (p, q)


def encode_message(message: str, k: int) -> list[int]:
    """Encodes a message into blocks of length k."""
    message = message.upper().ljust((len(message) + k - 1) // k * k)  # Pad with spaces
    blocks = [message[i:i + k] for i in range(0, len(message), k)]
    return [sum((ALPHABET.index(ch) * (27 ** (k - j - 1))) for j, ch in enumerate(block)) for block in blocks]


def decode_message(blocks: list[int], k: int) -> list[str]:
    """Decodes blocks of integers into a message."""
    decoded = []
    for block in blocks:
        temp = []
        for _ in range(k):
            temp.append(ALPHABET[block % 27])
            block //= 27
        decoded.append("".join(reversed(temp)))
    return decoded


def encrypt(blocks: list[int], public_key: int) -> list[int]:
    """Encrypts blocks using the Rabin Cryptosystem."""
    return [pow(block, 2, public_key) for block in blocks]


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Computes the extended Euclidean algorithm."""
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - (a // b) * y


def chinese_remainder(mp: int, mq: int, p: int, q: int) -> list[int]:
    """Applies the Chinese Remainder Theorem to combine solutions."""
    n = p * q
    _, yp, yq = extended_gcd(p, q)
    root1 = (mp * q * yq + mq * p * yp) % n
    root2 = (mp * q * yq - mq * p * yp) % n
    return [root1, n - root1, root2, n - root2]

def decrypt(ciphertext: list[int], private_key: tuple[int, int], public_key: int) -> list[int]:
    """Decrypts a ciphertext using the Rabin Cryptosystem."""
    p, q = private_key
    plaintexts = []
    for c in ciphertext:
        mp = pow(c, (p + 1) // 4, p)
        mq = pow(c, (q + 1) // 4, q)
        roots = chinese_remainder(mp, mq, p, q)
        plaintexts.append(roots)
    return plaintexts


def select_correct_plaintext(possible_plaintexts: list[int], k: int) -> list[int]:
    """Filters out valid plaintexts that map correctly to the alphabet."""
    valid = []
    for roots in possible_plaintexts:
        valid += [r for r in roots if all(0 <= (r // (27 ** i)) % 27 < 27 for i in range(k))]
    return valid

if __name__ == "__main__":
    k = 9  # Block size for plaintext
    l = 10  # Block size for ciphertext

    public_key, private_key = generate_key()
    print(f"Public Key (n): {public_key}")
    print(f"Private Key (p, q): {private_key}")

    message = input("Enter a message to encrypt: ")
    plaintext_blocks = encode_message(message, k)
    print(f"Encoded plaintext blocks: {plaintext_blocks}")

    ciphertext = encrypt(plaintext_blocks, public_key)
    print(f"Ciphertext blocks: {ciphertext}")

    decrypted_blocks = decrypt(ciphertext, private_key, public_key)
    valid_plaintext_blocks = select_correct_plaintext(decrypted_blocks, k)
    for i, block in enumerate(valid_plaintext_blocks):
        print(f"Possible plaintexts for block {i}: {block}")

    decoded_message = decode_message(valid_plaintext_blocks, k)
    for message in decoded_message:
        print(f"Decoded message: {message}")
