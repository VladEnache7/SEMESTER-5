from __future__ import annotations


class Grammar:
    """
    A class representing a formal grammar with non-terminals, terminals, a start symbol, and productions.
    """
    non_terminals: set[str]
    terminals: set[str]
    start_symbol: str
    productions: dict[str, list[list[str]]]

    def __init__(self, file_path):
        """
        Initialize a Grammar object.

        Args:
            non_terminals (set[str]): The set of non-terminal symbols.
            terminals (set[str]): The set of terminal symbols.
            start_symbol (str): The start symbol of the grammar.
            productions (dict[str, list[list[str]]]): The production rules, where each non-terminal maps to a list of production lists.
        """
        self.from_file(file_path)

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

            if not Grammar._validate(non_terminals, terminals, start_symbol, productions):
                return f"Grammar in {filepath} is not valid"

            self.non_terminals = non_terminals
            self.terminals = terminals
            self.start_symbol = start_symbol
            self.productions = productions
            return self

    @staticmethod
    def _parse_line(line: str) -> list[str]:
        """
        Parse a line containing a set definition.

        Args:
            line (str): The line to parse.

        Returns:
            list[str]: A list of elements in the set.
        """
        return line.split('=', maxsplit=1)[1].strip().split()

    @staticmethod
    def _parse_productions(lines: list[str]) -> dict[str, list[list[str]]]:
        """
        Parse production rules from lines.

        Args:
            lines (list[str]): The lines representing production rules.

        Returns:
            dict[str, list[list[str]]]: A dictionary of production rules.
        """
        productions = {}
        for line in lines:
            if not line:
                continue
            lhs, rhs = map(str.strip, line.split('->'))
            rhs_variants = [variant.strip().split() for variant in rhs.split('|')]
            productions.setdefault(lhs, []).extend(rhs_variants)
        return productions

    @staticmethod
    def _validate(non_terminals: set[str], terminals: set[str], start_symbol: str,
                  productions: dict[str, list[list[str]]]) -> bool:
        """
        Validate the grammar's consistency.

        Args:
            non_terminals (set[str]): The set of non-terminals.
            terminals (set[str]): The set of terminals.
            start_symbol (str): The start symbol.
            productions (dict[str, list[list[str]]]): The production rules.

        Returns:
            bool: True if the grammar is valid, False otherwise.
        """
        # Check if the start symbol is a valid non-terminal
        if start_symbol not in non_terminals:
            return False

        for left_hand_side, right_hand_side_variants in productions.items():
            # Check if the left-hand side is a valid non-terminal
            if left_hand_side not in non_terminals:
                return False
            # Check if the right-hand side contains only non-terminals and terminals
            for right_hand_side in right_hand_side_variants:
                if any(symbol not in non_terminals and symbol not in terminals for symbol in right_hand_side):
                    return False
        return True

    def is_context_free_grammar(self) -> bool:
        """
        Check if the grammar is a Context-Free Grammar (CFG).

        Returns:
            bool: True if the grammar is CFG, False otherwise.
        """
        return all(lhs in self.non_terminals for lhs in self.productions)

    def get_productions_for(self, non_terminal: str) -> list[list[str]]:
        """
        Retrieve the productions for a given non-terminal.

        Args:
            non_terminal (str): The non-terminal to retrieve productions for.

        Returns:
            list[list[str]]: The list of production rules for the non-terminal.

        Raises:
            ValueError: If the non-terminal is not valid.
        """
        if non_terminal not in self.non_terminals:
            raise ValueError(f"'{non_terminal}' is not a valid non-terminal.")
        return self.productions.get(non_terminal, [])

    def __str__(self) -> str:
        """
        String representation of the grammar.

        Returns:
            str: The string representation of the grammar.
        """
        return ("<------------> Grammar <------------>\n"
                f"Non-terminals: {self.non_terminals}\n"
                f"Terminals: {self.terminals}\n"
                f"Start Symbol: {self.start_symbol}\n"
                f"Productions: {self.productions}\n"
                "<----------------------------------->")


if __name__ == "__main__":
    # Test the Grammar class
    grammar = Grammar('.txt')
    print(grammar)
    print("Is Contex free grammar: ", grammar.is_context_free_grammar())