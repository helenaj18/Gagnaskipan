class Node:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        self.size = 0

    
    def push_front(self, value):
        new_node = Node(value, self.head)
        self.size += 1
        self.head = new_node
    
    def __str__(self):
        ret_str = ''
        n = self.head
        
        while n!= None:
            ret_str += str(n.data) + ' '
            n=n.next

        return ret_str
    
    def pop_front(self):

        if self.head == None:
            ret_val = None
        else:
            ret_val = self.head.data
            self.head = self.head.next
            self.size -= 1
        
        return ret_val

    def push_back(self, value):
        new_node = Node(value)
        new_node.next = None

        if self.get_size() == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size +=1


    def get_size(self):
        return self.size