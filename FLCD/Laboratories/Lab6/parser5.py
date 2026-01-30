from parser_out import ParserOutput, TreeNode

class RecursiveDescentParser:
    def __init__(self, grammar, input_string):
        self.grammar = grammar
        self.input = input_string.split()
        self.current_pos = 0
        self.stack = []  # Stack for backtracking
        self.parsed_stack = []  # Current sequence of symbols being parsed
        self.production_sequence = []  # To track applied productions
        self.parse_tree = ParserOutput(self.grammar.terminals, self.grammar.non_terminals)  # Parse tree output

    def expand(self, nonterminal, prod_index=0):
        """Expand a nonterminal using the specified production index."""
        if nonterminal in self.grammar.productions:
            production = self.grammar.productions[nonterminal][prod_index]
            self.stack.append((nonterminal, prod_index, self.current_pos, len(self.parsed_stack)))  # Push state
            self.production_sequence.append((nonterminal, production))  # Track production
            self.parsed_stack = production.split() + self.parsed_stack  # Add production to parsed stack
        else:
            raise ValueError(f"No production for {nonterminal}")

    def advance(self):
        if self.current_pos < len(self.input) and self.parsed_stack:
            next_symbol = self.parsed_stack.pop(0)
            if next_symbol == self.input[self.current_pos]:
                self.current_pos += 1
                return True
            else:
                self.parsed_stack.insert(0, next_symbol)  # Push it back
                return False
        return False

    def back(self):
        if self.stack:
            # Pop the last saved state
            nonterminal, prod_index, prev_pos, stack_size = self.stack.pop()

            # Restore the previous position in the input
            self.current_pos = prev_pos

            # Restore the stack to the state it was before expanding the production
            self.parsed_stack = self.parsed_stack[:stack_size]
            self.production_sequence.pop()

            # Try the next production for the same nonterminal
            return self.another_try(nonterminal, prod_index)

        # If the stack is empty, backtracking is not possible
        return False

    def another_try(self, nonterminal, prod_index):
        """Try the next production of the nonterminal."""
        prod_list = self.grammar.productions.get(nonterminal, [])
        if prod_index + 1 < len(prod_list):
            self.expand(nonterminal, prod_index + 1)  # Expand using the next production
            return True
        return False

    def success(self):
        """Check if parsing succeeded."""
        return self.current_pos == len(self.input) and not self.parsed_stack

    def parse(self):
        if not self.grammar.start_symbol:
            raise ValueError("Grammar must have a start symbol defined.")

        self.expand(self.grammar.start_symbol)

        while True:
            # If parsing succeeds
            if self.success():
                self.parse_tree.build_tree(self.production_sequence)
                return True

            # If there's something to parse
            if self.parsed_stack:
                next_symbol = self.parsed_stack[0]

                # If next symbol is a terminal, try to match it
                if next_symbol in self.grammar.terminals:
                    if not self.advance():
                        # If matching fails, backtrack
                        if not self.back() and len(self.stack) <= 1:
                            return False
                elif next_symbol in self.grammar.nonterminals:
                    # Expand nonterminal
                    self.parsed_stack.pop(0)
                    self.expand(next_symbol)
                else:
                    # Handle unexpected symbols
                    print(f"Error: Unexpected symbol {next_symbol}")
                    return False
            else:
                if not self.back() and len(self.stack) <= 1:
                    return False
    def print_parse_tree(self):
        """Prints the parse tree to the screen."""
        self.parse_tree.print_to_screen()

    def save_parse_tree(self, filename):
        """Saves the parse tree representation to a file."""
        self.parse_tree.save_to_file(filename)
