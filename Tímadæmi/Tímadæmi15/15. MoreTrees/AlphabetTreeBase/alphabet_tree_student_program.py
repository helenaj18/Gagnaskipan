
import sys

class TreeNode:
    def __init__(self, word = ""):
        self.word = word
        self.children = []

class AlphabetTree:
    def __init__(self):
        self.root = TreeNode('')

    def add_word(self, word):
        if word == '':
            return self.root
        
        node = self.add_word(word[:-1])

        for child_node in self.root.children:
            if child_node.word == word:
                return child_node
    

        new_node = TreeNode(word)
        self.root.children.append(new_node)

    
    def print_all(self):
        self.print_preorder_recur(self.root)
        print('')


    def print_preorder_recur(self, node):
        if node == None:
            return

        print(str(node.word))

        for child_node in node.children:
            self.print_preorder_recur(child_node)


    def print_leaves(self):
        return self.print_leaves_recur(self.root)

    def print_leaves_recur(self, node):
        if node.children == []:
            print(node.word)
        
        for child_node in node.children:
            self.print_leaves_recur(child_node)



if __name__ == "__main__":
    file = open(sys.path[0] + "/alphabet_words.txt")
    
    tree = AlphabetTree()
    
    for line in file:
        tree.add_word(line.strip())
    
    tree.print_all()
    tree.print_leaves()
    
    file.close()
