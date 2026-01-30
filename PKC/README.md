
# 🔐 Public-Key Cryptography

This course delves into the mathematical foundations of asymmetric cryptography. Unlike applied security courses that teach you *how* to use SSL/TLS, this course teaches you *why* the underlying algorithms (RSA, Rabin, ElGamal) are secure, focusing on Number Theory, Abstract Algebra, and Complexity Theory.

### 📅 Weekly Syllabus

The curriculum progresses from basic modular arithmetic to advanced cryptosystems.
Laboratories are held **every 2 weeks**.

| Week | 👨‍🏫 Lecture Content | 💻 Laboratory Schedule (Bi-weekly) |
|:---:|:---|:---|
| **1** | **Introduction:** Classical Cryptography (Caesar, Vigenère) | *No Lab* |
| **2** | **Foundations:** Algorithm Complexity & Number Theory | **Lab 1:** Classical Ciphers & Complexity |
| **3** | **RSA:** The RSA Cryptosystem & Key Generation | *No Lab* |
| **4** | **Primes:** Primality Testing (Miller-Rabin, Fermat) | **Lab 2:** Modular Arithmetics & Primality |
| **5** | **Factoring:** Integer Factorization Algorithms | *No Lab* |
| **6** | **Rabin:** Quadratic Residues & Rabin Cryptosystem | **Lab 3:** Factoring Integers & Rabin |
| **7** | **Algebra:** Polynomials & Finite Fields ($GF(p^n)$) | *No Lab* |
| **8** | **ElGamal:** The ElGamal Cryptosystem | **Lab 4:** Public-Key Cryptosystems (ElGamal/RSA) |
| **9** | **Discrete Log:** Algorithms for Computing Discrete Logs | *No Lab* |
| **10** | **Polynomials:** Factorization (Berlekamp’s algorithm) | **Lab 5:** Polynomials & Discrete Logs |
| **11** | **Signatures:** Digital Signature Schemes (DSA) | *No Lab* |
| **12** | **Protocols:** Key Exchange (Diffie-Hellman) | **Lab 6:** Practical Aspects & Signatures |
| **13** | **Practical:** Real-world constraints & Side-channel attacks | *No Lab* |
| **14** | **Advanced:** Elliptic-Curve Cryptography (ECC) | **Lab 7:** Final Evaluation / ECC |

---

### 💻 Laboratory & Algorithms

The laboratories are bi-weekly sessions focused on implementing mathematical algorithms from scratch (usually without using high-level crypto libraries) to understand their inner workings.

#### 🧪 Lab 1: Classical Ciphers
*   Implementing substitution and transposition ciphers.
*   Cryptanalysis of simple ciphers (Frequency analysis).

#### 🧪 Lab 2: Modular Arithmetic & Primality
*   **GCD:** Implementing the Extended Euclidean Algorithm.
*   **Modular Inverses:** Calculating $a^{-1} \pmod n$.
*   **Primality Testing:** Implementing probabilistic tests like **Miller-Rabin** or **Fermat** to find large primes.

#### 🧪 Lab 3: Integer Factorization
*   Attacking RSA by factoring the modulus $N$.
*   Algorithms: **Pollard's $\rho$** (rho) or **Fermat's Factorization Method**.

#### 🧪 Lab 4: Public-Key Systems
*   Full implementation of a cryptosystem (RSA, Rabin, or ElGamal).
*   Key generation, Encryption, and Decryption routines.
*   Handling padding schemes (conceptual).

#### 🧪 Lab 5 & 6: Advanced Topics
*   **Discrete Logarithms:** Implementing Baby-step Giant-step or Pollard's rho for logs.
*   **Signatures:** Implementing Digital Signature algorithms (DSA/RSA-PSS).
*   **Key Exchange:** Implementing Diffie-Hellman protocols.

---

### 🧠 Key Theoretical Concepts

<details>
<summary><strong>Click to expand detailed topic list</strong></summary>

#### I. Number Theory
*   **Euclidean Algorithm:** Finding GCD and linear combinations.
*   **Euler's Totient Theorem:** The basis for RSA decryption ($a^{\phi(n)} \equiv 1 \pmod n$).
*   **Chinese Remainder Theorem (CRT):** Used for optimizing RSA decryption.
*   **Quadratic Residues:** Used in the Rabin cryptosystem.

#### II. The "Hard" Problems
*   **Integer Factorization Problem (IFP):** Given $N = p \cdot q$, find $p$ and $q$. (Basis of RSA).
*   **Discrete Logarithm Problem (DLP):** Given $g$ and $h = g^x \pmod p$, find $x$. (Basis of ElGamal/Diffie-Hellman).

#### III. Algebraic Structures
*   **Finite Fields:** Arithmetic over $GF(2^n)$, essential for AES and Elliptic Curves.
*   **Polynomial Arithmetic:** Irreducible polynomials and modular arithmetic with polynomials.

</details>

---

### 🛠️ Resources & Tools

*   **Programming Languages:** C++, Python, or Java (BigInteger support is crucial).
*   **Tools:**
    *   **SageMath:** Excellent for prototyping algebraic algorithms.
    *   **WolframAlpha:** For verifying number theory calculations.

---

> *"Cryptography is the art of transforming information so that it is unintelligible to an unauthorized recipient."*