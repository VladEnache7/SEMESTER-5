
# 🔡 Formal Languages and Compiler Design

This course covers the mathematical foundations of programming languages and the practical engineering of compilers. The curriculum bridges the gap between high-level code and machine execution, moving systematically from **Lexical Analysis** (Scanning) to **Syntax Analysis** (Parsing) and finally to **Code Generation**.

### 📅 Weekly Syllabus

The course is split into theoretical lectures and practical seminars/labs involving the implementation of mini-language compiler components.

| Week | 👨‍🏫 Lecture Content | 📝 Seminar & Lab Focus |
|:---:|:---|:---|
| **1** | **Intro:** Compiler structure & Phases | **Lab 1 Start:** Definition of a Mini-Language (BNF) |
| **2** | **Scanning:** Lexical Analysis basics | **Lab 1 Cont:** Scanner implementation |
| **3** | **Formal Langs:** Grammars & Finite Automata | **Lab 1 Cont:** Symbol Table Organization |
| **4** | **Regular Langs:** Regex, FA equivalence, Pumping Lemma | **Lab 1 Due:** Scanner finalization & Testing |
| **5** | **Context-Free:** CFGs and Syntax Trees | **Lab 2 Start:** Finite Automata (FA) & Regular Grammars |
| **6** | **Parsing I:** General classification | **Lab 2 Due:** FA <-> RG Transformations |
| **7** | **Parsing II:** Recursive-Descent Parser | **Lab 3 Start:** Context-Free Grammars (CFG) |
| **8** | **Parsing III:** LL(1) Parsing | **Lab 3 Due:** CFG Transformations |
| **9** | **Parsing IV:** LR(k) and LR(0) Parsing | **Lab 4 Start:** **The Parser** (Team Project) |
| **10** | **Parsing V:** SLR, LR(1), LALR Parsers | **Lab 4 Cont:** Implementation of core parsing logic |
| **11** | **Tools:** Lexer/Parser generators (Lex/Yacc) | **Lab 4 Cont:** Module integration |
| **12** | **Attributes:** Attribute Grammars & Intermediary Code | **Lab 4 Cont:** Testing on formal grammars |
| **13** | **Optimization:** Code optimization & generation | **Lab 4 Due:** Testing on Mini-Language |
| **14** | **Automata:** Push-Down Automata (PDA) & Turing Machines | **Lab 5:** Usage of Lex/Yacc tools |

---

### 💻 Laboratory Projects

The laboratory work is sequential, requiring the invention of a simple programming language and the step-by-step construction of a compiler for it.

#### 🧪 Task 1: The Scanner (Lexical Analyzer)
*   **Goal:** Definition of a "Mini-Language" and development of a program that breaks source code into tokens.
*   **Key Concepts:**
    *   **BNF (Backus-Naur Form):** Formal specification of language syntax.
    *   **Symbol Table:** Efficient storage of variable names (using HashMaps or Binary Trees).
    *   **Tokenization:** Classification of input into identifiers, constants, keywords, and operators.

#### 🧪 Task 2: Finite Automata & Regular Grammars
*   **Goal:** Implementation of the mathematical models underlying the scanner.
*   **Key Concepts:**
    *   Representation of Finite Automata (FA) in code.
    *   Transformation of Regular Grammars into FAs and vice versa.

#### 🧪 Task 3: Context-Free Grammars (CFG)
*   **Goal:** Manipulation of structures that define programming logic (loops, if-statements).
*   **Key Concepts:**
    *   Elimination of ambiguity in grammars.
    *   Preparation of grammars for parsing.

#### 🧪 Task 4: The Parser (Syntax Analyzer)
*   *Note: Typically executed in teams of 2.*
*   **Goal:** Implementation of a specific parsing algorithm (Recursive Descent, LL(1), or LR(0)) to build a parse tree from the tokens generated in Task 1.
*   **Key Concepts:**
    *   **Syntax Trees:** Hierarchical representation of code.
    *   **Derivations:** Validation that a string belongs to a language.
    *   **Error Handling:** Detection of syntax errors (e.g., missing semicolons).

#### 🧪 Task 5: Compiler Tools
*   **Goal:** Re-implementation of the scanner and parser using standard industry tools.
*   **Tools:** **Lex** (Flex) and **Yacc** (Bison).

---

### 📚 Key Topics Breakdown

<details>
<summary><strong>Click to expand detailed topic list</strong></summary>

#### Part I: The Front-End (Analysis)
*   **Lexical Analysis:** Reading the stream of characters and grouping them into meaningful sequences (tokens).
*   **Syntax Analysis:** Determining if the tokens form a valid structure according to the grammar.
*   **Semantic Analysis:** Checking for type consistency (e.g., ensuring a String is not added to an Integer).

#### Part II: Formal Language Theory
*   **Chomsky Hierarchy:**
    *   Type 3: Regular Languages (Regex, Finite Automata).
    *   Type 2: Context-Free Languages (Push-Down Automata).
    *   Type 1: Context-Sensitive.
    *   Type 0: Recursively Enumerable (Turing Machines).

#### Part III: Parsing Algorithms
*   **Top-Down:** Begins from the root (Program) and attempts to match leaves (Tokens).
    *   *Examples:* Recursive Descent, LL(1).
*   **Bottom-Up:** Begins from the leaves and attempts to reduce them to the root.
    *   *Examples:* LR(0), SLR, LR(1), LALR.

</details>

---

### 🛠️ Resources & Tools

*   **Implementation Language:** Typically Python, Java, C++, or C# (Choice depends on student preference).
*   **Lex/Flex:** A tool for generating scanners.
*   **Yacc/Bison:** A tool for generating parsers.
*   **JFLAP:** Software for visualizing Automata and Grammars.

---

> *"A compiler is a program that translates a program written in one language into an equivalent program written in another language."*
