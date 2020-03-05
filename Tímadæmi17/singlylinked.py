class Node:

    def __init__(self, data_tuple = None, next = None):
        self.data_tuple = data_tuple
        self.next = next


class PriorityQueue_SLL:

    def __init__(self):
        self.head = None
        self.size = 0
    
# miða við að lægsta priority sé það sem er removeað fyrst
    def _insert_ordered(self, a_tuple, node):
        value = a_tuple[0]
        priority = a_tuple[1]

        if node == None:
            return Node((value,priority), node)
        
        elif priority < node.data_tuple[1]:
            new_node = Node((value, priority), node)
            return new_node
        
        else:
            node.next = self._insert_ordered(a_tuple, node.next)
            return node
    
    def insert_ordered(self, value, priority):
        a_tuple = (value, priority)
        self.head = self._insert_ordered(a_tuple, self.head)

    def pop_front(self):
        ret_val = self.head.data_tuple[0]

        if self.head != None:
            self.head = self.head.next
        
        return ret_val
    

    def __str__(self):

        a_str = ''
        n = self.head

        while n != None:
            a_str += str(n.data_tuple[0]) + ' '
            n = n.next
        
        return a_str



P = PriorityQueue_SLL()

P.insert_ordered(5,1)
print(P)
P.insert_ordered(3,3)
P.insert_ordered(5,2)
print(P)
P.pop_front()
print(P)