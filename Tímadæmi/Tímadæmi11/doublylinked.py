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


class DLL_Deque(DLL):

    # Þarf ekki að gera init því nkl eins


    def push_front(self, value):
        new_node = Node(self.head, self.head.next, value)
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1


    def push_back(self, value):
        new_node = Node(self.tail.prev, self.tail, value)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1

    
    def pop_front(self):
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.size -= 1


    def pop_back(self):
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1


    def get_value_front(self):
        return self.head.next.data

    def get_value_back(self):
        return self.tail.prev.data


class DLL_PosList(DLL):
    
    def __init__(self):
        DLL.__init__(self)
        self.curr_pos = 0
        self.curr_node = self.tail

    
    def insert(self, value):
        new_node = Node(self.curr_node.prev, self.curr_node, value)
        self.curr_node.prev.next = new_node
        self.curr_node.prev = new_node

        self.curr_node = new_node
        self.size +=1

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



lis = DLL_Deque()
print('PUSH FRONT 1 og 2')
lis.push_front(1)
lis.push_front(2)
print(lis)

print('POP FRONT')
lis.pop_front()
print(lis)

print('PUSH BACK 3x')
lis.push_back(2)
lis.push_back(3)
lis.push_back(4)
print(lis)

print('POP FRONT')
lis.pop_front()
print(lis)


print('POP BACK')
lis.pop_back()
print(lis)

print('GET FIRST VALUE GET LAST VALUE')
a = lis.get_value_front()
b = lis.get_value_back()

print(a,b)

print('PRINT LIST BACKWARDS')
lis.print_list()

print('GET SIZE')
print(lis.get_size())



print('\nPROFA POS LIST')


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