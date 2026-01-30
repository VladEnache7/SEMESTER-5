from enum import Enum
import re

from Lab6.FiniteAutomata import FiniteAutomata
from symbols_tables import SymbolTable


class TokenType(Enum):
    """Enumeration for token types, used to differentiate between reserved words, operators, and separators."""
    RESERVED_WORD = 0
    OPERATOR = 1
    SEPARATOR = 2


class Scanner:
    """
    Scanner class responsible for analyzing a source code file and breaking it into tokens.
    It categorizes tokens as identifiers, constants, operators, or separators, and manages
    the population of a Program Internal Form (PIF) and symbol tables.
    """

    def __init__(self, tokensFile: str = "token.in", programFile: str = "fake.vladpy"):
        """
        Initializes the scanner with program and token file paths, and sets up data structures
        for constants, identifiers, and reserved symbols.

        Args:
            programFile (str): Path to the file containing the program code.
            tokensFile (str): Path to the file defining reserved words, operators, and separators.
        """
        self.symbol_table = SymbolTable()  # Symbol table for constants and identifiers
        self.symbol_table_no = 1  # Unique ID counter for constants
        self.pif = []  # Program Internal Form (PIF) to track token occurrences
        self.programFile = programFile  # Program file path
        self.tokensFile = tokensFile  # Token file path
        self.reserved_words = {}  # Dictionary for reserved words
        self.operators = {}  # Dictionary for operators
        self.separators = {}  # Dictionary for separators
        self.finite_automata = FiniteAutomata('FA.in')

        self.parse_tokens()  # Parse tokens file to populate reserved words, operators, and separators

    def scan_program(self):
        """
        Scans the program file line by line, tokenizing each line and categorizing each token
        into constants, identifiers, operators, or separators. Valid tokens are added to the PIF.
        """
        with open(self.programFile, 'r') as program:
            if program is None:
                if 'q0' in self.finite_automata.final_states:
                    print("The program is accepted by the FA.")
                else:
                    print("The program is not accepted by the FA.")
                return
            for idx, line in enumerate(program):
                line = line[:-1]  # Remove newline character from each line
                tokens_with_spaces = re.split(
                    r'(&&|\|\||<=|>=|!=|==|\+=|-=|/=|\*=|[;,!+\-/*=<>[\](){}])', line
                )
                for token_with_spaces in tokens_with_spaces:

                    # Check if token is a string constant enclosed in quotes
                    if (token_with_spaces.startswith('"') and token_with_spaces.endswith('"')) or \
                            (token_with_spaces.startswith("'") and token_with_spaces.endswith("'")):
                        original_string = token_with_spaces.replace('"', '').replace("'", '')
                        if self.symbol_table.get(original_string) is None:
                            self.symbol_table.add(original_string, self.symbol_table_no)
                            self.symbol_table_no += 1
                    else:
                        # Split token and evaluate each part
                        for token in token_with_spaces.split():
                            # Check if token is an operator, separator, or reserved word
                            if token in self.operators or token in self.separators or token in self.reserved_words:
                                self.pif.append((token, -1))  # Append with placeholder -1 for reserved symbols

                            # Check if token is a valid identifier
                            elif Scanner.is_valid_identifier(token):
                                if self.symbol_table.get(token) is None:
                                    self.symbol_table.add(token, self.symbol_table_no)
                                    self.pif.append(("id", self.symbol_table_no))
                                    self.symbol_table_no += 1

                            # Check if token is a valid integer constant
                            elif Scanner.is_valid_constant(token):
                                if self.symbol_table.get(token) is None:
                                    self.symbol_table.add(token, self.symbol_table_no)
                                    self.pif.append(("const", self.symbol_table_no))
                                    self.symbol_table_no += 1

                            else:
                                print(f"Lexical error at line {idx} with token {token}!")
                                return  # Exit on lexical error

        self.save_pif()  # Save PIF to output file
        self.save_symbol_table()  # Save constants and identifiers to output file

    def save_pif(self):
        """Writes the Program Internal Form (PIF) to an output file."""
        with open('pif.out', 'w') as pif_file:
            for token, value in self.pif:
                pif_file.write(f"{token} -> {value}\n")

    def save_symbol_table(self):
        """Writes constants and identifiers from symbol tables to an output file."""
        with open('ST.out', 'w') as st_file:
            for key, value in self.symbol_table.get_all():
                st_file.write(f"{key} -> {value}\n")

    def parse_tokens(self):
        """
        Parses the token definition file to populate dictionaries of reserved words, operators, and separators.
        Identifies each section in the token file and assigns tokens to their respective types.
        """
        line_no = 1
        tokenType = TokenType
        with open(self.tokensFile, 'r') as tokens:
            for line in tokens:
                line = line.rstrip('\n')
                # Determine the token type based on file sections
                if line == '[reserved_words]':
                    tokenType = TokenType.RESERVED_WORD
                elif line == '[operators]':
                    tokenType = TokenType.OPERATOR
                elif line == '[separators]':
                    tokenType = TokenType.SEPARATOR
                # Add token to the appropriate dictionary
                elif tokenType == TokenType.RESERVED_WORD:
                    self.reserved_words[line] = line_no
                elif tokenType == TokenType.SEPARATOR:
                    self.separators[line] = line_no
                elif tokenType == TokenType.OPERATOR:
                    self.operators[line] = line_no

                line_no += 1

    def is_valid_identifier(self, string) -> bool:
        return self.finite_automata.check_word_if_identifier(string)

    def is_valid_constant(self, string) -> bool:
        return self.finite_automata.check_word_if_integer_constant(string)




if __name__ == "__main__":
    # Main execution: Initialize the Scanner with program and token files
    scanner = Scanner('p1.vladpy', 'token.in')
    scanner.scan_program()
