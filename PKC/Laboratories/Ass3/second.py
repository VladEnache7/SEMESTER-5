import math
from sympy import mod_inverse, gcd, nextprime

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


# Function to map ciphertext to numeric blocks
def ciphertext_to_blocks(ciphertext, block_size=3):
    nums = []
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]
        num = 0
        for ch in block:
            num = num * 27 + char_to_num[ch]
        nums.append(num)
    return nums


# Decrypt a numeric block
def decrypt_block(block, d, n):
    return pow(block, d, n)


# Function to convert numeric plaintext blocks back to letters
def blocks_to_plaintext(blocks, block_size=2):
    plaintext = ""
    for block in blocks:
        chars = []
        for _ in range(block_size):
            chars.append(num_to_char[block % 27])
            block //= 27
        plaintext += "".join(reversed(chars))
    return plaintext


def print_text_in_blocks(s, l):
    # Remove any whitespace for clean blocks (optional)
    s = s.replace(" ", "")

    # Divide the text into blocks of size l
    blocks = [s[i:i + l] for i in range(0, len(s), l)]

    # Print each block
    for block in blocks:
        print(block)


# Decrypt ciphertext message
def decrypt_message(ciphertext, p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = find_encryption_exponent(phi_n)  # Automatically find the smallest valid e
    d = mod_inverse(e, phi_n)  # Calculate modular inverse of e
    k = 2  # plaintext block size
    l = 3  # ciphertext block size

    print(f"n (p * q): {n}")
    print(f"φ(n) ((p-1) * (q-1)): {phi_n}")
    print(f"Encryption exponent (e): {e}")
    print(f"Decryption exponent (d): {d}")

    # Step 1: Convert ciphertext to numeric blocks
    ciphertext_blocks = ciphertext_to_blocks(ciphertext, l)
    print(f"Ciphertext blocks (size {l}): {ciphertext_blocks}")
    print_text_in_blocks(ciphertext, l)

    # Step 2: Decrypt numeric blocks
    plaintext_blocks = [decrypt_block(block, d, n) for block in ciphertext_blocks]
    # print(f"Plaintext numeric blocks: {plaintext_blocks}")

    # Step 3: Convert numeric blocks to letters
    plaintext = blocks_to_plaintext(plaintext_blocks, k)
    print_text_in_blocks(plaintext, k)
    print(f"Decrypted plaintext blocks (size {k}): {plaintext_blocks}")
    print(f"Decrypted plaintext: {plaintext}")
    return plaintext


# Main program to take inputs and run decryption
if __name__ == "__main__":
    print("RSA Decryption")
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    ciphertext = input("Enter the ciphertext to decrypt: ").strip()

    plaintext = decrypt_message(ciphertext, p, q)
    print("\nFinal Decrypted plaintext:", plaintext)