
import sys
from enum import Enum

class DivisionByZero(Exception):
    pass

class UnknownInTree(Exception):
    pass

class OutputFormat(Enum):
    PREFIX = 0
    INFIX = 1
    POSTFIX = 2



class TreeNode:
    def __init__(self, data = '', left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


class Tokenizer:
    def __init__(self, str_statement):
        self.statement = str_statement
        self.position = 0

    def get_next_token(self):
        i = self.position
        while i < len(self.statement) and self.statement[i] != " ":
            i += 1
        ret_val = self.statement[self.position:i]
        self.position = i + 1
        return ret_val


class PrefixParseTree:
    def __init__(self):
        self.root = None
        self.format = 'prefix'

    def load_statement_string(self, statement):
        tokenizer = Tokenizer(statement)
        self.root = self.load_statement_string_recur(tokenizer, self.root)

    def load_statement_string_recur(self, tokenizer, node):

        token = tokenizer.get_next_token()

        if node is self.root:
            self.root = TreeNode(token)
            self.load_statement_string_recur(tokenizer, self.root.left)
        
        elif node == None and not (token in ['+', '-', '*', '/']):
            return TreeNode(token)
        
        elif node.left == None:
            node.left = self.load_statement_string_recur(tokenizer, node.left)
            
        
        elif node.right == None:
            node.right = self.load_statement_string_recur(tokenizer, node.right)
        
        return node


    def set_format(self, out_format):
        if out_format == 'INFIX':
            self.format == 'infix'
        
        elif out_format == 'POSTFIX':
            self.format == 'postfix'

    def root_value(self):
        pass

    def simplify_tree(self):
        pass

    def solve_tree(self, root_value):
        pass


    def str_prefix(self, node):
        if node == None:
            return

        return str(node.data) + ' ' + self.str_prefix(node.left) + self.str_prefix(node.right)


    def str_infix(self, node):
        if node == None:
            return ''
        
        
        return self.str_infix(node.left) + str(node.data) + ' ' + self.str_infix(node.right)
    

    def str_postfix(self, node):
        if node == None:
            return

        return self.str_prefix(node.left) + self.str_prefix(node.right) + ' ' + str(node.data)


    def __str__(self):

        if self.format == 'prefix':
            a_str = self.str_prefix(self.root)
        
        elif self.format == 'infix':
            a_str = self.str_infix(self.root)
        
        elif self.format == 'postfix':
            a_str = self.str_postfix(self.root)

        return a_str

statement = ''

# This is a tester function to test that
# the output and/or error message from the
# prefix_tree operations are correct.
def test_prefix_parser(str_statement, solve = False, root_value = 0):

    if solve == True:
        prefix_tree = PrefixParseTree()
        prefix_tree.load_statement_string(str_statement)
        print("PREFIX: " + str(prefix_tree))
        print("The value of x if the root_value is " + str(root_value) + " is: " + str(prefix_tree.solve_tree(root_value)))
    else:
        prefix_tree = PrefixParseTree()
        prefix_tree.load_statement_string(str_statement)
        print("PREFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.INFIX)
        print("INFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.POSTFIX)
        print("POSTFIX: " + str(prefix_tree))

        str_print = "The value of the tree is: "
        try:
            str_print += str(prefix_tree.root_value())
        except DivisionByZero:
            str_print += str("A division by zero occurred")
        except UnknownInTree:
            str_print += str("There is an unknown value in the tree")
        print(str_print)

        print("SIMPLIFIED:")
        prefix_tree.simplify_tree()
        prefix_tree.set_format(OutputFormat.PREFIX)
        print("PREFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.INFIX)
        print("INFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.POSTFIX)
        print("POSTFIX: " + str(prefix_tree))

    print("\n\n")


if __name__ == "__main__":
    org_out = sys.stdout
    fout = open(sys.path[0] + "/parse_out.txt", "w+")
    sys.stdout = fout
    f = open(sys.path[0] + "/prefix_statements.txt", "r")
    previous_line = None
    for line in f:
        some_split = line.split()
        if some_split[0] == "solve":
            test_prefix_parser(previous_line.strip(), True, int(some_split[1]))
        test_prefix_parser(line.strip())
        previous_line = line
    f.close()
    sys.stdout = org_out
    fout.close()
