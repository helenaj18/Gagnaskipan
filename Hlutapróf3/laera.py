# Tímadæmi 14

class BinaryNode:

    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self, root = None):
        self.root = root
    

    def _populate_tree_recur(self, level = 0):
        data_str = input()

        if data_str == '':
            return None

        level += 1
        print(level * '   |' + '--LEFT, level ' + str(level)+ ': ', end= ' ')
        left_node = self._populate_tree_recur(level)
        print(level * '   |' + '--RIGHT, level ' + str(level)+ ': ', end= ' ')
        right_node = self._populate_tree_recur(level)

        return BinaryNode(data_str, left_node, right_node)
    
    def populate_tree(self):
        print('ROOT :', end = ' ')
        self.root = self._populate_tree_recur()
    
    def print_preorder(self):
        self._preorder(self.root)
        print()

    def print_inorder(self):
        self._inorder(self.root)
        print()
    
    def print_postorder(self):
        self._postorder(self.root)
        print()
    

    def _preorder(self, node):
        
        if node == None:
            return
        
        print(str(node.data), end = ' ')
        self._preorder(node.left)
        self._preorder(node.right)
    
    def _inorder(self, node):

        if node == None:
            return
        
        self._inorder(node.left)
        print(str(node.data), end = ' ')
        self._inorder(node.right)
    
    def _postorder(self, node):

        if node == None:
            return

        self._postorder(node.left)
        self._postorder(node.right)
        print(str(node.data), end = ' ')
    

# bt = BinaryTree()

# bt.populate_tree()
# bt.print_preorder()
# bt.print_inorder()
# bt.print_postorder()

class GeneralNode():

    def __init__(self, data = None):
        self.data = data
        self.children = []


class GeneralTree:

    def __init__(self, root = None):
        self.root = root
    
    def populate_tree(self):
        print('ROOT: ', end = '')
        self.root = self._populate_tree_recur()
    
    def _populate_tree_recur(self, level = 0):

        data_str = input()

        if data_str == '':
            return None

        level += 1
        node = GeneralNode(data_str)

        while True:
            print(level * '    |' + '--level {}:'.format(level), end = ' ')
            child_node = self._populate_tree_recur(level)
            if child_node == None:
                break
            
            node.children.append(child_node)

        return node
    
    def print_preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, node):
        if node == None:
            return
        print(str(node.data), end = ' ')
        for child in node.children:
            self._preorder(child)
    
    def _print_postorder_recur(self, node):
        if node == None:
            return
        for child_node in node.children:
            self._print_postorder_recur(child_node)
        print(str(node.data), end = " ")

    def print_postorder(self):
        self._print_postorder_recur(self.root)
        print("")



# gt = GeneralTree()
# gt.populate_tree()
# gt.print_preorder()
# gt.print_postorder()


# tímadæmi 15
class TreeNode:
    def __init__(self, data = ""):
        self.data = data
        self.children = []

    def add_word(self, word, length = 1):
        if length > len(word):
            return
        
        word_part = word[:length]

        for child in self.children:
            if child.data == word_part:
                child.add_word(word, length+1)
                return
        
        child = TreeNode(word_part)

        for index in range(len(self.children)):
            if self.children[index].data > word_part:
                self.children.insert(index, child)
                child.add_word(word, length+1)
                return
        
        self.children.append(child)
        child.add_word(word, length+1)
    
    def print_preorder(self):
        print(self.data)
        for child in self.children:
            child.print_preorder()
    
    def print_leaves(self):
        if len(self.children) == 0:
            print(self.data)
        for child in self.children:
            child.print_leaves()
            

import sys

class AlphabetTree:
    def __init__(self):
        self.root = TreeNode()
    
    def add_word(self, word):
        self.root.add_word(word)
    
    def print_all(self):
        self.root.print_preorder()

    def print_leaves(self):
        self.root.print_leaves()



if __name__ == "__main__":
    file = open(sys.path[0] + "/alphabet_words.txt")
    
    tree = AlphabetTree()
    
    for line in file:
        tree.add_word(line.strip())
    
    tree.print_all()
    tree.print_leaves()
    
    file.close()
