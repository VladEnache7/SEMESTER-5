from __future__ import annotations

from Lab6.parser_out import ParserOutput
from scanner import Scanner
from scanner import Scanner
from FiniteAutomata import FiniteAutomata

class Grammar:
    non_terminals: set[str]
    terminals: set[str]
    start_symbol: str
    productions: dict[str, list[list[str]]]

    def __init__(self, file_path: str, scanner: Scanner, finite_automata: FiniteAutomata):
        result = self.from_file(file_path)
        self.scanner = scanner
        self.finite_automata = finite_automata
        if isinstance(result, str):
            raise ValueError(result)

    def from_file(self, filepath: str) -> Grammar | str:
        """
        Create a Grammar instance from a file.

        Args:
            filepath (str): The path to the file containing grammar definitions.

        Returns:
            Union[Grammar, str]: A Grammar instance if the file is valid; otherwise, an error message.
        """
        with open(filepath, 'r', encoding='utf-8') as file:
            non_terminals = set(Grammar._parse_line(file.readline()))
            terminals = set(Grammar._parse_line(file.readline()))
            start_symbol = file.readline().split('=')[1].strip()
            file.readline()  # Skip the empty line
            productions = Grammar._parse_productions([line.strip() for line in file])

            if not Grammar._validate(non_terminals=non_terminals, terminals=terminals, start_symbol=start_symbol,
                                     productions=productions):
                return f"Grammar in {filepath} is not valid"

            self.non_terminals = non_terminals
            self.terminals = terminals
            self.start_symbol = start_symbol
            self.productions = productions
            return self

    @staticmethod
    def _parse_line(line: str) -> list[str]:
        return line.split('=', maxsplit=1)[1].strip().split()

    @staticmethod
    def _parse_productions(lines: list[str]) -> dict[str, list[list[str]]]:
        productions = {}
        for line in lines:
            if not line:
                continue
            lhs, rhs = map(str.strip, line.split('->'))
            rhs_variants = [variant.strip().split() for variant in rhs.split('|')]
            productions.setdefault(lhs, []).extend(rhs_variants)
        return productions

    @staticmethod
    def _validate(non_terminals: set[str], terminals: set[str], start_symbol: str, productions: dict[str, list[list[str]]]) -> bool:
        if start_symbol not in non_terminals:
            print(f"Error: Start symbol '{start_symbol}' is not in non-terminals.")
            return False

        for left_hand_side, right_hand_side_variants in productions.items():
            if left_hand_side not in non_terminals:
                print(f"Error: LHS '{left_hand_side}' is not a valid non-terminal.")
                return False
            for right_hand_side in right_hand_side_variants:
                for symbol in right_hand_side:
                    if symbol != 'ε' and symbol not in non_terminals and symbol not in terminals and not Grammar.is_digit_or_letter(symbol):
                        print(f"Error: Symbol '{symbol}' in production '{left_hand_side} -> {right_hand_side}' is neither a terminal nor a non-terminal.")
                        return False
        return True

    @staticmethod
    def is_digit_or_letter(symbol: str):
        return symbol.isalnum() or symbol == '_' or symbol == "..."

    def is_context_free_grammar(self) -> bool:
        return all(lhs in self.non_terminals for lhs in self.productions)

    def get_productions_for(self, non_terminal: str) -> list[list[str]]:
        if non_terminal not in self.non_terminals:
            raise ValueError(f"'{non_terminal}' is not a valid non-terminal.")
        return self.productions.get(non_terminal, [])

    def __str__(self) -> str:
        return ("<------------> Grammar <------------>\n"
                f"Non-terminals: {self.non_terminals}\n"
                f"Terminals: {self.terminals}\n"
                f"Start Symbol: {self.start_symbol}\n"
                f"Productions: {self.productions}\n"
                "<----------------------------------->")

from parser_out import ParserOutput, TreeNode

class RecursiveDescentParser:
    def __init__(self, grammar, input_string):
        self.grammar = grammar
        self.input = input_string.split()
        self.current_pos = 0
        self.stack = []
        self.parsed_stack = []
        self.production_sequence = []
        self.parse_tree = ParserOutput(self.grammar.terminals, self.grammar.non_terminals)

    def expand(self, nonterminal, prod_index=0):
        if nonterminal in self.grammar.productions:
            production = self.grammar.productions[nonterminal][prod_index]
            self.stack.append((nonterminal, prod_index, self.current_pos, len(self.parsed_stack)))
            self.production_sequence.append((nonterminal, production))
            if not self.grammar.finite_automata.check_word_if_identifier(production) and production != ['a']:
                self.parsed_stack = production + self.parsed_stack
        else:
            raise ValueError(f"No production for {nonterminal}")

    def advance(self):
        if self.current_pos < len(self.input) and self.parsed_stack:
            next_symbol = self.parsed_stack.pop(0)
            if next_symbol == self.input[self.current_pos]:
                self.current_pos += 1
                return True
            else:
                self.parsed_stack.insert(0, next_symbol)
                return False
        return False

    def back(self):
        if self.stack:
            nonterminal, prod_index, prev_pos, stack_size = self.stack.pop()
            self.current_pos = prev_pos
            self.parsed_stack = self.parsed_stack[:stack_size]
            self.production_sequence.pop()
            return self.another_try(nonterminal, prod_index)
        return False

    def another_try(self, nonterminal, prod_index):
        prod_list = self.grammar.productions.get(nonterminal, [])
        if prod_index + 1 < len(prod_list):
            self.expand(nonterminal, prod_index + 1)
            return True
        return False

    def success(self):
        return self.current_pos + 1 == len(self.input) and not self.parsed_stack

    def parse(self):
        if not self.grammar.start_symbol:
            raise ValueError("Grammar must have a start symbol defined.")
        self.expand(self.grammar.start_symbol)
        while True:
            if self.success():
                self.parse_tree.build_tree(self.production_sequence)
                return True
            if self.parsed_stack:
                next_symbol = self.parsed_stack[0]
                if next_symbol in self.grammar.terminals:
                    if not self.advance():
                        if not self.back() and len(self.stack) <= 1:
                            return False
                elif next_symbol in self.grammar.non_terminals:
                    self.parsed_stack.pop(0)

                    self.expand(next_symbol)
                else:
                    print(f"Error: Unexpected symbol {next_symbol}")
                    return False
            else:
                if not self.back() and len(self.stack) <= 1:
                    return False

    def print_parse_tree(self):
        self.parse_tree.print_to_screen()

    def save_parse_tree(self, filename):
        self.parse_tree.save_to_file(filename)
