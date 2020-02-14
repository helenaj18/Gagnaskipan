class Empty(Exception):
    pass


class Node:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedQueue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    
    def push(self, data):
        
        if self.get_size() == 0:
            new_node = Node(data)
            new_node.next = None
            self.head = new_node
            self.tail = new_node
            self.size +=1
        else:
            new_node = Node(data)
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
            self.size +=1

    def pop(self):
        if self.head == None:
            raise Empty()
        else:
            self.head = self.head.next
            self.size -= 1


    def get_size(self):
        return self.size
    

    def __str__(self):

        ret_str = ''
        current_node = self.head

        while current_node != None:
            ret_str += str(current_node.data)+ "\n"
            current_node = current_node.next

        return ret_str.strip()  

q = LinkedQueue()
print('PUSH')
q.push('A')
q.push('B')
q.push('C')
q.push('D')
q.push('E')
print(q)

print('POP 2x')

q.pop()
q.pop()
print(q)
