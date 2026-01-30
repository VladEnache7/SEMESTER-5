import math
from sympy import gcd, nextprime

# Define the 27-character alphabet
alphabet = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
char_to_num = {ch: i for i, ch in enumerate(alphabet)}
num_to_char = {i: ch for ch, i in char_to_num.items()}


# Function to calculate the smallest valid odd prime e
def find_encryption_exponent(phi_n):
    e = 3
    while gcd(e, phi_n) != 1:
        e = nextprime(e)
    return e


# Function to map plaintext to numeric blocks
def plaintext_to_blocks(plaintext, block_size=2):
    plaintext = plaintext.upper()
    nums = [char_to_num[ch] for ch in plaintext]
    blocks = []
    for i in range(0, len(nums), block_size):
        block = nums[i:i + block_size]
        # Combine to single number (e.g., AB -> 01 02 -> 102)
        combined = sum(n * (27 ** (block_size - 1 - idx)) for idx, n in enumerate(block))
        blocks.append(combined)
    return blocks


# Encrypt a numeric block
def encrypt_block(block, e, n):
    return pow(block, e, n)


# Function to convert numeric ciphertext back to letter blocks
def blocks_to_ciphertext(blocks, block_size=3):
    ciphertext = ""
    for block in blocks:
        chars = []
        for _ in range(block_size):
            chars.append(num_to_char[block % 27])
            block //= 27
        ciphertext += "".join(reversed(chars))
    return ciphertext


def print_text_in_blocks(s, l):
    # Remove any whitespace for clean blocks (optional)
    s = s.replace(" ", "")

    # Divide the text into blocks of size l
    blocks = [s[i:i + l] for i in range(0, len(s), l)]

    # Print each block
    for block in blocks:
        print(block)


# Encrypt plaintext message
def encrypt_message(plaintext, p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = find_encryption_exponent(phi_n)
    k = 2  # plaintext block size
    l = 3  # ciphertext block size

    # Step 1: Calculate blocks and encrypt
    plaintext_blocks = plaintext_to_blocks(plaintext, k)
    ciphertext_blocks = [encrypt_block(block, e, n) for block in plaintext_blocks]

    # Print detailed steps
    print(f"n (p*q): {n}")
    print(f"φ(n) ((p-1)*(q-1)): {phi_n}")
    print(f"e (encryption exponent): {e}")
    print_text_in_blocks(plaintext, k)
    print(f"Plaintext blocks (size {k}): {plaintext_blocks}")

    # Numerical equivalents and encryption
    for i, block in enumerate(plaintext_blocks):
        print(f"c{i + 1} (block {block}^e mod n): {ciphertext_blocks[i]}")

    # Ciphertext in letter blocks
    encrypted_message = blocks_to_ciphertext(ciphertext_blocks, l)
    print(f"Encrypted message blocks (size {l}): {encrypted_message}")
    print_text_in_blocks(encrypted_message, l)
    return encrypted_message


# Main program to take inputs and run encryption
if __name__ == "__main__":
    print("RSA Encryption")
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    plaintext = input("Enter the plaintext to encrypt: ").strip()

    ciphertext = encrypt_message(plaintext, p, q)
    print("\nFinal Encrypted ciphertext:", ciphertext)