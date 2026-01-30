from FiniteAutomata import FiniteAutomata
from symbols_tables import SymbolTable
from scanner import Scanner
from grammar import Grammar, RecursiveDescentParser
from FiniteAutomata import  FiniteAutomata

finite_automata = FiniteAutomata('FA.in')

scanner = Scanner('token.in', 'p1.vladpy')

grammar = Grammar('myPythonGrammar.txt', scanner, finite_automata)

input_string = ""
parser = RecursiveDescentParser(grammar, input_string)
print("Started Parsing")
if parser.parse():
    print("True")
    print(parser.parse_tree.transform_representation())
else:
    print("False")
