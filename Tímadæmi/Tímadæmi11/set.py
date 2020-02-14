class Node:

    def __init__(self, prev = None, next = None, data = None):
        self.prev = prev
        self.next = next
        self.data = data


class DLL:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get_size(self):
        return self.size



    def print_list(self):
        
        n = self.tail.prev
        a_str = ''

        while n != self.head:
            a_str += str(n.data) + ' '
            n=n.prev
        
        print(a_str.strip())
    

    def __str__(self):
        ret_str = ''
        n = self.head.next
        
        while n!= self.tail:
            ret_str += str(n.data) + ' '
            n=n.next

        return ret_str


class DLL_Set(DLL):


    def add_value(self, value):
        new_node = Node(self.head, self.head.next, value)
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1

    def remove_value(self,value):
        pass

    def __contains__(self, value):
        pass

    def __str__(self):
        pass
