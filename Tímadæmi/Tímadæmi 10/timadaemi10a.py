class Node:

    def __init__(self, prev = None, next = None, data = None):
        self.prev = prev
        self.next = next
        self.data = data


class DLL_Deque:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0


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


    def __str__(self):
        ret_str = ''
        n = self.head.next
        
        while n!= self.tail:
            ret_str += str(n.data) + ' '
            n=n.next

        return ret_str
    
    def print_list(self):
        
        n = self.tail.prev
        a_str = ''

        while n != self.head:
            a_str += str(n.data) + ' '
            n=n.prev
        
        print(a_str.strip())
    
    def get_size(self):
        return self.size


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