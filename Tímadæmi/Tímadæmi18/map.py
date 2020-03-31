class KeyError(Exception):
    pass

class Node:

    def __init__(self, data = None, next = None):
        self.next = next
        self.data = data

class Linked_list:

    def __init__(self, head = None):
        self.head = head
        self.size = 0


    def push_front(self, a_tuple):
        new_node = Node(a_tuple, self.head)
        self.size += 1
        self.head = new_node
    

    def remove(self, node):
        '''Removes a node from a linked list'''

        n = self.head
        if self.head == node:
            self.head = self.head.next

        else:

            while n.next != None:
                if n.next == node:
                    n.next = n.next.next

                if n.next != None:
                    n = n.next
        
    def __contains__(self, val):
        '''Returns True if a linked list 
        contains value, else False'''

        n = self.head
        if n != None:
            while n != None:
                if n.data.name == val:
                    return True
                n = n.next

        return False

        
    def __str__(self):
        ret_str = ''
        n = self.head
        
        while n!= None:
            ret_str += str(n.data) + ' '
            n=n.next

        return ret_str


# class Item:
#     def __init__(self, key = None, value = None):
#         self.key = key
#         self.value = value

class Map:

    def __init__(self, key = None, value = None):
       # self.item = Item(key, value) - örgl fínt að gera eh tímann svona
        self.ls = Linked_list()
        self.size = 0
    

    def insert(self, key, value):
        a_tuple = (key,value)
        self.ls.push_front(a_tuple)
        self.size += 1


    def find(self, key):
        n = self.ls.head

        while n != None:
            if key == n.data[0]:
                return n.data[1]
            n = n.next
        
        else:
            raise KeyError() 


    def update(self, key, value):
        n = self.ls.head
        while n!= None:

            if n.data[0] == key:
                try:
                    self.find(n.data[0])
                    n.data = (key,value)
                
                except KeyError:
                    self.insert(key, value)

            n = n.next


    def remove(self, key):
        n = self.ls.head

        while n != None:
            if key == n.data[0]:
                self.size -= 1
                return self.ls.remove(n)
            n = n.next
    
        else:
            raise KeyError() 


    def __len__(self):
        return self.size
    

    def __str__(self):
        
        a_str = ''

        n = self.ls.head

        while n!= None:
            a_str += str(n.data)
            n = n.next
        
        return a_str


m = Map()
m.insert(3,'h')
m.insert(4, 'b')
print(m)
print(m.find(3))
m.update(3, 'a')
print(m)
m.remove(3)
print(m)
print(len(m))