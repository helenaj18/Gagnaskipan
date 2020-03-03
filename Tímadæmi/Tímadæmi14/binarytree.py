class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right



class BinaryTree:

    def __init__(self):
        self.root = None

    def _populate_tree_recur(self, level = 0):
        data_str = input()

        if data_str == '':
            return None

        level += 1
        print(level * '   |' + '--LEFT, level ' + str(level)+ ': ', end= ' ')
        left_node = self._populate_tree_recur(level)
        print(level * '   |' + '--RIGHT, level ' + str(level)+ ': ', end= ' ')
        right_node = self._populate_tree_recur(level)

        return Node(data_str, left_node, right_node)

    def populate_tree(self):
        print('ROOT :', end = ' ')
        self.root = self._populate_tree_recur()
    

    def print_preorder_recur(self, node):
        if node == None:
            return
        
        print(str(node.data), end =' ')
        self.print_preorder_recur(node.left)
        self.print_preorder_recur(node.right)
    
    def print_preorder(self):
        self.print_preorder_recur(self.root)
        print('')
    
    def count_values_recur(self, value, node):
        counter = 0

        if node == None:
            return 0

        elif node.data == value:
            counter += 1
        
        counter += self.count_values_recur(value, node.left)
        counter += self.count_values_recur(value, node.right)

        return counter
    
    def count_values(self, value):
        return self.count_values_recur(value, self.root)
    

    def change_value_recur(self, val_1, val_2, node):
        if node == None:
            return
        elif node.data == val_1:
            node.data = val_2
        
        self.change_value_recur(val_1, val_2, node.left)
        self.change_value_recur(val_1, val_2, node.left)
        
    
    def change_value(self, val_1, val_2):
        return self.change_value_recur(val_1, val_2, self.root)
    

# Mín tilraun
    def change_daughter_recur(self, value, node):
        if node.left == None or node.right == None:
            return

        elif node.right.data == value:
            node.right.data = node.data
        
        else:
            node.left.data = node.data
        
        self.change_daughter_recur(value, node.left)
        self.change_daughter_recur(value, node.right)
    
# Kennara tilraun
    def change_daughter_recur1(self, value, node, parent):
        if node == None:
            return
        if node.data == value:
            if parent != None:
                temp = node.data
                node.data = parent.data
                parent.data = temp
        
        self.change_daughter_recur1(value, node.left, node)
        self.change_daughter_recur1(value, node.right, node)
        
    
    def change_daughter(self, value):
        return self.change_daughter_recur1(value, self.root, None)


    def print_inorder_recur(self, node):
        if node == None:
            return
        
        self.print_inorder_recur(node.left)
        print(str(node.data), end =' ')
        self.print_inorder_recur(node.right)
    

    def print_inorder(self):
        self.print_inorder_recur(self.root)
        print('')
    

    def print_postorder_recur(self, node):
        if node == None:
            return
        
        self.print_postorder_recur(node.left)
        self.print_postorder_recur(node.right)
        print(str(node.data), end =' ')
    

    def print_postorder(self):
        self.print_postorder_recur(self.root)
        print('')



bt = BinaryTree()
bt.populate_tree()
bt.print_preorder()
bt.print_inorder()
bt.print_postorder()
print(bt.count_values('A'))
# bt.change_value('A','B')
# bt.print_preorder()
bt.change_daughter('B')
bt.print_preorder()


class GeneralNode():
    def __init__(self, data = None):
        self.data = data
        self.children = []
    

class GeneralTree:

    def __init__(self, root = None):
        self.root = root
    
    def populate_tree_recur(self, level = 0):
        data_str = input()

        if data_str == '':
            return None
        level += 1
        node = GeneralNode(data_str)
        while True:
            print(level * '    |' + '--level {}:'.format(level), end = ' ')
            child_node = self.populate_tree_recur(level)
            if child_node == None:
                break
            
            node.children.append(child_node)

        return node
    
    def populate_tree(self):
        print('ROOT :', end = ' ')
        self.root = self.populate_tree_recur()


    def print_preorder_recur1(self, node):
        if node == None:
            return

        print(str(node.data), end =' ')
        for child_node in node.children:
            self.print_preorder_recur1(child_node)


    def print_tree_preorder(self):
        self.print_preorder_recur1(self.root)
        print('')
    

    def print_inorder_recur(self, node):
        if node == None:
            return
        
        if node.children != []:
            self.print_inorder_recur(node.children[0])
        
        print(node.data, end = ' ')
        
        if node.children != []:
            for child_node in node.children[1:]:
                self.print_inorder_recur(child_node)
    
    def print_inorder(self):
        self.print_inorder_recur(self.root)
        print()

# Only preorder makes sense for a general tree but inorder tree works if i have instructions :D


# gt = GeneralTree()
# gt.populate_tree()
# gt.print_tree_preorder()
# gt.print_inorder()