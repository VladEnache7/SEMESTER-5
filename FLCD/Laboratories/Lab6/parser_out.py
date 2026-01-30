class TreeNode:
    def __init__(self, value, father=None):
        self.value = value        # Grammar symbol (terminal/nonterminal)
        self.father = father      # Parent node
        self.sibling = None       # Sibling node
        self.children = []        # List of children for easy access

    def add_child(self, child):
        """Adds a child to the current node."""
        if self.children:
            # Set sibling for the last child
            self.children[-1].sibling = child
        self.children.append(child)

    def __str__(self):
        """String representation of the node."""
        return self.value


class ParserOutput:
    def __init__(self, terminal, nonterminal):
        self.root = None  # Root of the parse tree
        self.terminal = terminal
        self.nonterminal = nonterminal

    def build_tree(self, production_sequence):
        """
        Builds the parse tree from a sequence of productions.
        :param production_sequence: List of (nonterminal, production) tuples
        """
        if not production_sequence:
            return None

        stack = []  # Stack for constructing the tree
        for nonterminal, production in production_sequence:
            if not self.root:
                # Create the root node
                self.root = TreeNode(nonterminal)
                stack.append(self.root)
                # Create nodes based on production
                current = stack.pop()
                symbols = production
                for symbol in symbols:
                    child = TreeNode(symbol, current)
                    current.add_child(child)
                    if symbol in self.nonterminal:  # Nonterminal
                        stack.append(child)
            else:
                # Create nodes based on production
                current = stack.pop()
                symbols = production
                for symbol in symbols:
                    child = TreeNode(symbol, current)
                    current.add_child(child)
                    if symbol in self.nonterminal:  # Nonterminal
                        stack.append(child)

    def transform_representation(self, node=None, level=0, index=1, parent_index=0, sibling_index=0):
        if node is None:
            node = self.root

        result = f"{index} {node.value} {parent_index} {sibling_index}\n"
        current_index = index
        for i, child in enumerate(node.children):
            sibling_index = current_index + 1 if i < len(node.children) - 1 else 0
            result += self.transform_representation(child, level + 1, current_index + 1, current_index, sibling_index)
            current_index += 1
        return result

    def print_to_screen(self):
        print(self.transform_representation())

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(self.transform_representation())