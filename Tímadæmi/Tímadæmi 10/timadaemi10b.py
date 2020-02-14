class Node:

    def __init__(self, prev = None, next = None, data = None):
        self.prev = prev
        self.next = next
        self.data = data



class DLL_PosList:


    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.curr_pos = 0
        self.curr_node = self.tail
    
    

    def insert(self, value):
        new_node = Node(self.curr_node.prev, self.curr_node, value)
        self.curr_node.prev.next = new_node
        self.curr_node.prev = new_node

        self.curr_node = new_node
        self.size +=1

    def __str__(self):
        ret_str = ''
        n = self.head.next
        
        while n!= self.tail:
            ret_str += str(n.data) + ' '
            n=n.next

        return ret_str
    

    def get_size(self):
        return self.size
    

    def print_list(self):
        n = self.tail.prev
        a_str = ''

        while n != self.head:
            a_str += str(n.data) + ' '
            n=n.prev
        
        print(a_str.strip())


    def move_to_next(self):

        if self.curr_pos != self.get_size()-1:
            self.curr_pos += 1
            self.curr_node = self.curr_node.next
        else:
            print('The position is at the back of the list!')


    def move_to_prev(self):

        if self.curr_pos != 0:
            self.curr_pos -= 1
            self.curr_node = self.curr_node.prev
        else:
            print('The position is at the front of the list!')


    def get_value(self):
        return self.curr_node.data


    def remove(self):
        self.curr_node.prev.next = self.curr_node.next
        self.curr_node.next.prev = self.curr_node.prev

        self.curr_node = self.curr_node.next


lis = DLL_PosList()

print('INSERT')
lis.insert('A')
lis.insert('B')
lis.insert('C')
print(lis)


print('PRINT BACKWARDS')
lis.print_list()


print('MOVE')
lis.insert('A')
lis.insert('B')
lis.move_to_next()
lis.insert('C')
lis.move_to_prev()
lis.insert('D')
print(lis)

print('GET VALUE')

print(lis.get_value())

print('REMOVE')

lis.remove()
print(lis)

print('INSERT')
lis.insert('A')
lis.insert('B')
lis.insert('C')
print(lis)