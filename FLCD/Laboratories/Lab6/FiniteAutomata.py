from __future__ import annotations

import string


class FiniteAutomata:
    """
    A class to represent a Finite Automaton (FA).

    Attributes:
        states (list): A list of states in the FA.
        alphabet (list): A list of symbols in the FA's alphabet.
        transitions (dict): A dictionary representing the transitions in the FA.
                            Keys are tuples of (current_state, symbol) and values are the next state.
        initial_state (str): The initial state of the FA.
        final_states (list): A list of final states in the FA.
    """

    def __init__(self, file_path: str):
        """
        Initializes the FiniteAutomata object by reading the FA definition from a file.

        Args:
            file_path (str): The path to the file containing the FA definition.
        """
        self.states = []
        self.alphabet = []
        self.transitions: dict[tuple[str, str], str] = {}
        self.initial_state = ''
        self.final_states = []
        self.read_finite_automata_from_file(file_path)
        self.check_deterministic()
        # self.start_manu()

    def read_finite_automata_from_file(self, file_path: str):
        """
        Reads the FA definition from a file and populates the attributes.

        Args:
            file_path (str): The path to the file containing the FA definition.
        """
        with open(file_path, 'r') as file:
            for line in file:
                values = line.split('=')[1]
                if "all_states" in line:
                    self.states = values.split()
                elif "alphabet" in line:
                    self.alphabet = values.split()
                elif "initial_state" in line:
                    self.initial_state = values.strip()
                elif "final_states" in line:
                    self.final_states = values.split()
                elif "transitions" in line:
                    for transition in values.split(','):
                        start, operation, end = transition.split()
                        if operation == '[a-zA-Z]':
                            self.transitions.update({(start, letter): end for letter in string.ascii_letters})
                        elif operation == '[0-9]':
                            self.transitions.update({(start, digit): end for digit in string.digits})
                        elif operation == '[1-9]':
                            self.transitions.update({(start, digit): end for digit in string.digits[1:]})
                        elif operation == '[a-z]':
                            self.transitions.update({(start, letter): end for letter in string.ascii_lowercase})
                        elif operation == '[A-Z]':
                            self.transitions.update({(start, letter): end for letter in string.ascii_uppercase})
                        elif len(operation) == 1:
                            self.transitions[(start, operation)] = end

    def print_fa(self):
        """
        Prints the FA in a formatted manner.
        """
        print("M = {Q, E, RO, q0, F}")
        print(f"Q = {self.states}")
        print(f"E = {self.alphabet}")
        print(f"RO = {self.transitions}")
        print(f"q0 = {self.initial_state}")
        print(f"F = {self.final_states}")

    # def print_menu(self):
    #     """
    #     Prints the menu options for interacting with the FA.
    #     """
    #     print("1. Display the FA")
    #     print("2. Display the set of states")
    #     print("3. Display the alphabet")
    #     print("4. Display the transitions")
    #     print("5. Display the initial state")
    #     print("6. Display the final states")
    #     print("7. Verify constant")
    #     print("8. Verify identifier")
    #     print("x. Exit")

    # def start_manu(self):
    #     """
    #     Starts the menu for user interaction with the FA.
    #     """
    #     option = -1
    #
    #     while option != 'x':
    #         self.print_menu()
    #         option = input("Enter option: ")
    #         if option == '1':
    #             self.print_fa()
    #         elif option == '2':
    #             print(f"Q = {self.states}\n")
    #         elif option == '3':
    #             print(f"E = {self.alphabet}\n")
    #         elif option == '4':
    #             print(f"RO = {self.transitions}\n")
    #         elif option == '5':
    #             print(f"q0 = {self.initial_state}\n")
    #         elif option == '6':
    #             print(f"F = {self.final_states}\n")
    #         elif option == '7':
    #             word = input("Enter word to verify if it is a constant: ")
    #             if self.check_word_if_integer_constant(word):
    #                 print(f"{word} is a constant.\n")
    #             else:
    #                 print(f"{word} is not a constant.\n")
    #         elif option == '8':
    #             word = input("Enter word to verify if it is an identifier: ")
    #             if self.check_word_if_identifier(word):
    #                 print(f"{word} is an identifier.\n")
    #             else:
    #                 print(f"{word} is not an identifier.\n")
    #         elif option == 'x':
    #             break

    def check_word_if_integer_constant(self, word):
        """
        Checks if a given word is a valid integer constant according to the FA.

        Args:
            word (str): The word to check.

        Returns:
            bool: True if the word is a valid integer constant, False otherwise.
        """
        state = self.initial_state
        for letter in word:
            state = self.transitions.get((state, letter))
            if state is None:
                return

        if state in ['p3', 'p4']:
            return True
        return False

    def check_word_if_identifier(self, word):
        """
        Checks if a given word is a valid identifier according to the FA.

        Args:
            word (str): The word to check.

        Returns:
            bool: True if the word is a valid identifier, False otherwise.
        """
        state = 'p0'
        for letter in word:
            state = self.transitions.get((state, letter))
            if state is None:
                return

        if state in ['p1', 'p2']:
            return True
        return False

    def check_deterministic(self):
        """
        Checks if the finite automaton is deterministic.

        A finite automaton is deterministic if for each state and each symbol in the alphabet,
        there is at most one transition to a next state.

        Returns:
            bool: True if the finite automaton is deterministic, False otherwise.
        """
        for state in self.states:
            seen_symbols = set()
            for (current_state, symbol), next_state in self.transitions.items():
                if current_state == state:
                    if symbol in seen_symbols:
                        print(f"Non-deterministic transition from state {state} with symbol {symbol}")
                        return
                    seen_symbols.add(symbol)
        print("The finite automaton is deterministic.")


if __name__ == "__main__":
    finiteAutomaton = FiniteAutomata('FA.in')
    print(finiteAutomaton.check_word_if_identifier(""))
    print(finiteAutomaton.check_word_if_integer_constant(""))
    print(finiteAutomaton.check_word_if_identifier("ddx"))
    print(finiteAutomaton.check_word_if_identifier("12ddx"))
    print(finiteAutomaton.check_word_if_integer_constant("123"))
    print(finiteAutomaton.check_word_if_integer_constant("-123"))
    print(finiteAutomaton.check_word_if_integer_constant("ads123"))
    print(finiteAutomaton.check_word_if_integer_constant("123aa"))
    print(finiteAutomaton.check_word_if_integer_constant("0123"))
    finiteAutomaton.menu()