class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
    

    def push_back(self, data):
        new_node = Node(data) # vil að nóðan bendi á None því á að verða síðasta nóðan
        
        if self._head == None: # ef listinn er tómur, líka hægt að nota tail == None
            self._head = new_node
        else:
            self._tail.next = new_node
        
        self._tail = new_node

    
    def __str__(self):
        node = self._head
        ret_str = ''

        while node != None:
            ret_str += str(node.data) + "\n"
            node = node.next
        
        return ret_str

def push_front(head, data):
    new_node = Node(data, head)

    return new_node

# Með linked list klasa
# listinn = LinkedList()

# for i in range(1, 6):
#     listinn.push_back('string ' + str(i))

# print(listinn)



# Áður en við bjuggum ti LinkedList klasann


# Recursive fallið
def print_list(head):
    if head != None:
        print(head.data)
        print_list(head.next)


head = Node()
head.data = 'string 1'

for i in range(2, 6):
    head = push_front(head, 'string ' + str(i))

print_list(head)

# áður en ég bjó til print list
# node = head
# while node != None:
#     print(node.data)
#     node = node.next
        