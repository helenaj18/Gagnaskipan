from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue:

    def __init__(self, a_type):
        
        if a_type == 'array':
            self.instance = ArrayDeque()
        else:
            self.instance = LinkedList()

    
    def add(self, value):
        return self.instance.push_back(value)
    

    def remove(self):
        return self.instance.pop_front()
    
    def get_size(self):
        return self.instance.get_size()

