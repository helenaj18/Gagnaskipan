from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Stack():
    

    def __init__(self, a_type):
        
        if a_type == 'array':
            self.instance = ArrayDeque()
        else:
            self.instance = LinkedList()
    

    def push(self, value):
        return self.instance.push_front(value)
    

    def pop(self):
        return self.instance.pop_front()
    

    def get_size(self):
        return self.instance.get_size()

