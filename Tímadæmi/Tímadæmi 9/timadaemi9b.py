class Empty(Exception):
    pass


class Node:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedStack:
    
    def __init__(self):
        self.head = None
        self.size = 0

    
    def push(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        self.size += 1


    def pop(self):
        ans = self.head
        
        if self.head != None:
            self.head = self.head.next
            self.size -= 1
        else:
            raise Empty()

        return ans


    def get_size(self):
        return self.size


    def __str__(self):
        node = self.head
        ret_str = ''

        while node != None:
            ret_str += str(node.data) + "\n"
            node = node.next
        
        return ret_str.strip()


print('PUSH STACK')
s = LinkedStack()

s.push('A')
s.push('B')
print(s)

print('POP STACK')
s.pop()
print(s)

print('PRINT SIZE')
print(s.get_size())
