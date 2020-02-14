class Empty(Exception):
    pass


class Node:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    

def push_front(head, data):
    
    new_node = Node(data)
    new_node.next = head
    head = new_node

    return head


def print_contents(head):

    current_node = head

    while current_node != None:
        print(current_node.data)
        current_node = current_node.next


def print_contents_recursive(head):

    current_node = head

    if current_node != None:
        print(current_node.data)
        print_contents_recursive(current_node.next)


def pop_first(head):
    if head != None:
        head = head.next
        return head
    else:
        raise Empty


# Hægt að gera betur með encapsulating class eða bæta við tail
def push_back(head, data):

    current_node = head

    while current_node != None:
        current_node = current_node.next
    
    else:
        current_node = Node(data)
        head.next = current_node
    
    return head

# Er ekki flóknari en push back og front og pop first í implementi
# en tekur lengri tíma O(n) en push front og pop first
def pop_back(head):

    current_node = head

    while current_node.next.next != None:
        current_node = current_node.next
    
    else:
        current_node.next = None
    
    return current_node



head = Node('A')
head = push_front(head, 'B')


print('WHILE:')
print_contents(head)
print('RECURSIVE:')
print_contents_recursive(head)

print('POP FIRST')
head = pop_first(head)
print_contents(head)

print('PUSH BACK')
head = push_back(head, 'C')
print_contents(head)


print('POP BACK')
pop_back(head)
print_contents(head)
