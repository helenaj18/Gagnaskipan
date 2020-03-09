
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
    def __init__(self, data = '', left = None, right = None, parent = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        


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
        self.simple = False

    def load_statement_string(self, statement):
        tokenizer = Tokenizer(statement)
        self.root = self.load_statement_string_recur(tokenizer)
    
    def load_statement_string_recur(self, tokenizer, parent = None):
        token = tokenizer.get_next_token()
        new_node = TreeNode(token)
        new_node.parent = parent

        if token == '':
            return None
        elif token not in ['+', '-', '*', '/']:
            return TreeNode(token)
        
        new_node.left = self.load_statement_string_recur(tokenizer, new_node)
        new_node.right = self.load_statement_string_recur(tokenizer, new_node)
        
        return new_node
    

    def set_format(self, out_format):

        if out_format.name == 'PREFIX':
            self.format = 'prefix'

        elif out_format.name == 'INFIX':
            self.format = 'infix'
        
        elif out_format.name == 'POSTFIX':
            self.format = 'postfix'

    def root_value(self):
        return self.root_value_recur(self.root)

    def root_value_recur(self, n):

        while n != None:

            if n.data[-1].isdigit():
                return int(n.data)
            
            elif n.data == '+':
                return self.root_value_recur(n.left) + self.root_value_recur(n.right)

            elif n.data == '-':
                return self.root_value_recur(n.left) - self.root_value_recur(n.right)

            elif n.data == '*':
                return self.root_value_recur(n.left) * self.root_value_recur(n.right)

            elif n.data == '/':
                a = self.root_value_recur(n.left)
                b = self.root_value_recur(n.right)

                if b == 0:
                    raise DivisionByZero()
                
                return a/b
            else:
                raise UnknownInTree()
        
    
    def simplify_tree(self):
        self.simplify_tree_recur(self.root)
        self.simple = True

    def simplify_tree_recur(self, node):

        if node == None:
            return None

        try:
            node.data = str(self.root_value_recur(node))
            node.left = None
            node.right = None      
        except:
            self.simplify_tree_recur(node.left)
            self.simplify_tree_recur(node.right)
        


    # def simplify_tree_helper(self, node):

    #     if node != None:
    #         # Use [-1] to only get the number, not the negative sign if there is one
    #         if node.left.data[-1].isdigit() and node.right.data[-1].isdigit():
    #             if node.data == '+':
    #                 node.data = str(int(node.left.data) + int(node.right.data))
                
    #             elif node.data == '-':
    #                 node.data = str(int(node.left.data) - int(node.right.data))
                
    #             elif node.data == '*':
    #                 node.data = str(int(node.left.data) * int(node.right.data))
                
    #             elif node.data == '/':
    #                 if int(node.right.data) == 0:
    #                     raise DivisionByZero()
                    
    #                 node.data = str(int(int(node.left.data) / int(node.right.data)))
                
    #             node.left = None
    #             node.right = None
                
    #             if not node is self.root:
    #                 return node.parent
                
    #             return node
            
                    
    #         elif node.left.data in ['+', '-', '*', '/']:
    #             return node.left
            
    #         elif node.right.data in ['+', '-', '*', '/']:
    #             return node.right
            
    #         else:
    #             return None


    def solve_tree(self, root_value):
        return self.solve_tree_recur(root_value, self.root)

    def solve_tree_recur(self, root_value, node):
        if self.simple != True:
            self.simplify_tree()

        if node.left != None and node.right != None:
            if node.left.data not in ['+', '-', '*', '/'] and not node.left.data.isdigit():
                if node.data == '+':
                    return root_value - int(node.right.data)
                
                elif node.data == '-':
                    return root_value + int(node.right.data)
            
            elif node.right.data not in ['+', '-', '*', '/'] and not node.right.data.isdigit():
                if node.data == '+':
                    return int(node.left.data) + root_value
                
                elif node.data == '-':
                    return int(node.left.data) - root_value

            else:
                self.solve_tree_recur(root_value, node.left)
                self.solve_tree_recur(root_value, node.right)
    
    def solve(self, root_value):
        a_str = self.str_infix(self.root)

        for letter in a_str:
            if letter == ' ' or letter == '(' or letter == ')':
                continue

            if letter == 'x':
                


    def str_prefix(self, node):
        if node == None:
            return ''

        return str(node.data) + ' ' + self.str_prefix(node.left) + self.str_prefix(node.right)


    def str_infix(self, node):
        a_str = ''
        space = ''

        if node == None:
            return ''
        
        if node.left != None:
            a_str += '('
            space = ' '
        
        a_str += self.str_infix(node.left)
        a_str += space + str(node.data) + space
        a_str += self.str_infix(node.right)

        if node.right != None:
            a_str += ')'
        
        return a_str
    

    def str_postfix(self, node):
        if node == None:
            return ''

        return self.str_postfix(node.left) + self.str_postfix(node.right) + str(node.data) + ' '


    def __str__(self):


        if self.format == 'prefix':
            a_str = self.str_prefix(self.root)
        
        elif self.format == 'infix':
            a_str = self.str_infix(self.root)
        
        elif self.format == 'postfix':
            a_str = self.str_postfix(self.root)

        return a_str

statement = ''

pp = PrefixParseTree()
pp.load_statement_string('- + - x 5 + 6 3 4')
print(pp.solve_tree(12))

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


if __name__ != "__main__":
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
