class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Set_BST:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def add(self, value):
        if self.contains(value) == False:
            self.root = self._add(value, self.root)
            self.size += 1
    
    def _add(self, value, node):
        
        if node == None:
            return TreeNode(value)

        elif node.value > value:
            node.left =  self._add(value, node.left)
        
        elif node.value < value:
            node.right = self._add(value, node.right)
        
        return node

    
    def contains(self, value):
        return self._contains(value, self.root)
    

    def _contains(self, value, node):

        if node == None:
            return False
        
        elif value < node.value:
            return self._contains(value, node.left)
        
        elif node.value < value:
            return self._contains(value, node.right)
        
        else:
            return True
    
    def remove(self, value):
        self.root = self._remove(value, self.root)

    
    def _remove(self, value, node):
        if node == None:
            return node
        
        elif node.value == value:

            if node.left == None and node.right == None:
                return None
            
            elif node.left != None and node.right != None:
                #rightmost af vinstra
                swapnode = self.find_rightmost(node.left)
                # þarf ekki að svissa, bara setja swapnode gildið í n nóðuna
                node.value = swapnode.value
                
                # node left er rótin í trénu sem við erum að leita í núna
                node.left = self._remove(node.value, node.left)

                return node

            elif node.left == None:
                return node.right
            
            else:
                return node.left
        
        elif value < node.value:
            node.left = self._remove(value, node.left)
            return node
        
        elif value < node.value:
            node.right = self._remove(value, node.right)
            return node
    

    def find_rightmost(self, node):
        
        while node.right != None:
            node = node.right
        
        return node

    

    def __len__(self):
        return self.size


    def __str__(self):
        a_str = self._inorder_recur(self.root)
        return a_str
    

    def _inorder_recur(self, node):
        if node == None:
            return ''
        
        # allt vinstra megin við mig, svo mig sjálfan og svo allt hægra megin við mig
        return self._inorder_recur(node.left) + str(node.value) + ' ' + self._inorder_recur(node.right)
    


s = Set_BST()
s.add(5)
s.add(3)
s.add(8)
s.add(2)
s.add(4)
print(s)
s.remove(3)
print(s)
print(s.contains(2))