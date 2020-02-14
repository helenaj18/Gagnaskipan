class Node:

    def __init__(self, data = None, next = None):
        self.next = next
        self.data = data

class Linked_list:

    def __init__(self, head = None):
        self.head = head
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
        self.head = self.head.next
        self.size -= 1
    

    def push_back(self, value):

        new_node = Node(value)
        curr = self.head

        while curr.next != None:
            curr = curr.next
        else:
            curr.next = new_node
        
        self.size += 1

    def pop_back(self):
        
        curr = self.head

        while curr.next.next != None:
            curr = curr.next
        else:
            curr.next = None
        
        self.size -= 1

    def get_size(self):
        return self.size



ll = Linked_list()
ll.push_front(5)
ll.push_front(7)
ll.push_front(8)
print(ll)
ll.pop_front()
print(ll)

ll.push_back(4)
print(ll)

ll.pop_back()
print(ll)
print(ll.get_size())