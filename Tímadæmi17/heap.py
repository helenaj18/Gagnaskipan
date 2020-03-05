class HeapNode:

    def __init__(self, priority, data = None, parent = None, left = None, right = None):
        self.priority = priority
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right


class PriorityQueue:

    def __init__(self):
        self.root = None
        self.last_node = None

    
    def add(self, priority, value):
        if self.root == None:
            self.last_node = self.root = HeapNode(priority, value)
        

        # síðasta nóða er vinstra barn
        elif self.last_node.parent != None and self.last_node is self.last_node.parent.left:
            self.last_node.parent.right = HeapNode(priority, value, self.last_node.parent)
            self.last_node = self.last_node.parent.right
        
        else:
            next_to_add = self.last_node

            while next_to_add is not self.root and next_to_add in next_to_add.parent.right:
                next_to_add = next_to_add.parent
            
            if next_to_add is not self.root:
                # einn upp og svo einn til hægri
                next_to_add = next_to_add.parent.right
            
            while next_to_add.left != None:
                next_to_add = next_to_add.left
            
            next_to_add.left = HeapNode(priority, value, next_to_add)

        # Laga röðina
        self.bubble_up()

    

    def bubble_up(self):
        '''Gets the order correct '''
        node = self.last_node

        while node.parent != None and node.priority < node.parent.priority:
            self.swap_values(node, node.parent)
            node = node.parent


    def remove(self):

        if self.last_node == None:
            return None
        
        ret_val = self.root.data

        if self.last_node is self.root:
            self.last_node = self.root = None
            return ret_val
        
        # víxlum annars gildum á last node og rótinni (sbr "regla")
        self.swap_values(self.last_node, self.root)

        if self.last_node is self.last_node.parent.right:
            self.last_node = self.last_node.parent.left
            self.last_node.parent.right = None
        
        else:
            self.last_node = self.last_node.parent
            self.last_node.left = None

            while self.last_node is not self.root and self.last_node is self.last_node.parent.left:
                self.last_node = self.last_node.parent
            
            if self.last_node is not self.root:
                # einn upp og svo einn til vinstri
                self.last_node = self.last_node.parent.left
            
            while self.last_node.right != None:
                self.last_node = self.last_node.right
        
        # Laga röðina
        self.bubble_down()
                
        return ret_val
    
    def bubble_down(self):
        '''Gets the order correct '''
        node = self.root
        # ef það er ekki vinstra barn þá er heldur ekki hægra barn
        while node.left != None:
            if node.right != None and node.right.priority < node.priority:

                if node.left.priority < node.right.priority:
                    self.swap_values(node, node.left)
                    node = node.left
                else:
                    self.swap_values(node, node.right)
                    node = node.right
            
            elif node.left.priority < node.priority:
                self.swap_values(node, node.left)
            
            else:
                # lægra en bæði börnin
                break

    def swap_values(self, node1, node2):
        temp_pri = node1.priority
        temp_val = node1.data
        node1.priority = node2.priority
        node1.value = node2.value
        node2.priority = temp_pri
        node2.value = temp_val
    


h = PriorityQueue()

h.add(5,1)
h.add(3,2)
h.add(4,3)
h.add(8,4)
h.add(6,5)
h.add(7,6)
h.add(2,7)
h.add(1,8)
h.add(9,9)

print(h.root.data)
print(h.root.left.data)
print(h.root.right.data)
# print(h.root.left.left.data)
# print(h.root.left.right.data)
# print(h.root.right.left.data)
# print(h.root.right.right.data)
# print(h.root.left.left.left.data)
