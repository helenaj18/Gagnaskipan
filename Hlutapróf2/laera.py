class Node:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next



def push_front(head, data):

    node = Node(data, head)
    
    return node

def print_(head):

    n = head

    while n != None:
        print(n.data)
        n = n.next

def printrecursive(head):
    
    if head != None:
        print(head.data)
        printrecursive(head.next)

def pop_first(head):
    if head != None:
        head = head.next
    
    return head

def push_back(head, data):
    n = head
    node = Node(data)

    while n.next != None:
        n = n.next
        
    else:
        n.next = node
    
    return head


def pop_back(head):
    n = head

    while n.next.next != None:
        n = n.next
    
    else:
        n.next = None
    
    return head





head = Node('A')
head = push_front(head, 'B')
printrecursive(head)
head = pop_first(head)
print_(head)

print('push back 2 og front B')
head = push_back(head, 2)
head = push_front(head, 'B')
printrecursive(head)

print('pop back')
head = pop_back(head)
print_(head)


class SLL_Stack:

    def __init__(self, head = None):
        self.head = head
        self.size = 0
    

    def push_front(self, value):

        node = Node(value, self.head)
        self.head = node
        self.size += 1
    
    def pop_front(self):
        ans = self.head

        if self.head != None:
            self.head = self.head.next
            self.size -= 1
        
        return ans

    def get_size(self):
        return self.size
    
    def __str__(self):

        n = self.head
        ret_str = ''

        while n != None:
            ret_str += str(n.data) + ' '
            n = n.next
        
        return ret_str


class SLL_QUEUE:

    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        self.size = 0
    
    
    def push_back(self, value):
        new_node = Node(value)

        if self.get_size() == 0:
            self.head = new_node
            self.tail = new_node
            self.size +=1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.size +=1
        
    
    def pop_front(self,value):
        ans = self.head

        if self.head != None:
            self.head = self.head.next
            self.size -= 1
        
        return ans
    

    def get_size(self):
        return self.size
    
    def __str__(self):

        n = self.head
        ret_str = ''

        while n != None:
            ret_str += str(n.data) + ' '
            n = n.next
            
        return ret_str

class Node1:

    def __init__(self, prev = None, next = None, data = None):
        self.prev = prev
        self.next = next
        self.data = data

class DLL_Deque:

    def __init__(self, head = None, tail= None):
        self.head = head
        self.tail = tail
        self.size = 0
    

    def push_front(self, value):
        node = Node1(self.head, self.head.next, value)
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def push_back(self, value):
        node = Node1(self.tail.prev, self.tail, value)
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1


    def pop_back(self):
        ret_val = self.tail.prev

        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.size -= 1

        return ret_val


    def pop_front(self):
        ret_val = self.head.next

        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.size -= 1

        return ret_val


    def get_val_front(self):
        if self.head.next != None:
            return self.head.next.data

    def get_val_back(self):
        if self.tail.prev != None:
            return self.tail.prev.data


    def __str__(self):
        ret_str = ''

        n = self.head.next

        while n != self.tail:
            ret_str += str(n.data) + ' '
            n = n.next
        
        return ret_str
    

    def print_backwards(self):

        n = self.tail.prev

        while n != self.head:
            print(str(n.data))
            n = n.prev
    
    def get_size(self):
        return self.size


class DLL_PosList:
    def __init__(self, head = None, tail= None):
        self.head = head
        self.tail = tail
        self.size = 0
        self.curr_node = self.tail
        self.curr_pos = 0
    


    def insert(self, value):
        
        node = Node1(self.curr_node.prev, self.curr_node, value)

        self.curr_node.prev.next = node
        self.curr_node.prev = node

        self.curr_node = node
        self.curr_pos += 1
    

    def __str__(self):
        n = self.head.next
        ret_str = ''
        while n != self.tail:
            ret_str += str(n.data)+' '
            n = n.next

        return ret_str
    
    def get_size(self):
        return self.size
    

    def print_backwards(self):

        n = self.tail.prev
        
        while n != self.tail:
            print(str(n.data), end = ' ')
            n = n.prev
    

    def move_to_next(self):

        if self.curr_pos != self.get_size()-1 and self.curr_node != None:
            self.curr_node = self.curr_node.next
            self.curr_pos += 1
    
    def move_to_prev(self):
        if self.curr_pos != 0 and self.curr_node != None:
            self.curr_node = self.curr_node.prev
            self.curr_pos -= 1
    

    def get_value(self):
        if self.curr_node != None:
            return self.curr_node.data
    
    def remove(self):
        self.curr_node.prev.next = self.curr_node.next
        self.curr_node.next.prev = self.curr_node.prev

        self.curr_node = self.curr_node.next


def headInsert(value, head):
    new_node = Node(value, head)
    return new_node


def printList(head):
    if head == None:
        print()
        return
    print(head.data, end=', ')
    printList(head.next)


def length(head):
    if head == None:
        return 0
    
    return 1 + length(head.next)

def sumlist(head):
    if head == None:
        return 0
    
    return head.data + sumlist(head.next)

def insert_ordered(head, value):
    
    if head == None:
        return Node(value, head)
    
    elif value < head.data:
        new_node = Node(value, head)
        return new_node
    
    else:
        head.next = insert_ordered(head.next, value)
        return head


def reverseList(head):

    if head.next == None:
        return head
    
    new_head = reverseList(head.next)
    head.next.next = head
    head.next = None
    return new_head


def merge_lists(head_one, head_two):
    if head_one == None:
        return head_two
    
    elif head_two == None:
        return head_one
    
    elif head_one.data < head_two.data:
        head_one.next = merge_lists(head_one.next, head_two)
        return head_one

    else:
        head_two.next = merge_lists(head_one, head_two.next)
        return head_two


def mergeSort(head):
    node = head
    node_half = head

    if head == None:
        return head
    
    elif head.next == None:
        return head

    else:
        node = node_half.next
        node_half.next = None
        return merge_lists(mergeSort(head), mergeSort(node))
    


head = headInsert(3, None)
printList(head)
print(length(head))
print(length(None))
print('Insert ordered')
head = insert_ordered(head,2)
printList(head)
head = reverseList(head)
printList(head)

head = mergeSort(head)
printList(head)
head = headInsert(4, head)
printList(head)
head = mergeSort(head)
printList(head)


# AUKA

# SINGLY
def push_front1(self,value):
    new_node = Node(value, self.head)
    self.head = new_node
    self.size += 1


def push_back1(self,value):
    new_node = Node(value)

    if self.size == 0:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node
        self.tail = new_node
    
    self.size += 1


def pop_front1(self):
    if self.size != 0:
        ret_val = self.head.data
        self.head = self.head.next
        self.size -= 1
    else:
        ret_val = None
    
    return ret_val

def pop_back1(self):
    n = self.head
    
    if self.head == self.tail:
        return None
    
    while n.next != self.tail:
        n = n.next
    
    else:
        ret_val = n.next.data
        n.next = n.next.next
        self.size -= 1
    
    return ret_val

def insert_ordered1(head, value):

    if head == None:
        return Node(value, head)
    
    elif value < head.data:
        new_node = Node(value, head.next)
        return new_node
    
    else:
        head.next = insert_ordered(head.next, value)
        return head

def reverse_lst(head):

    if head.next == None:
        return head
    
    new_head = reverse_lst(head.next)
    head.next.next = head
    head.next = None
    return new_head

def duplicate(head):

    if head.next == None:
        return head
    
    new_node = Node(head.data)
    new_node.next = duplicate(head.next)

# Doubly

def pushfront1(self,value):
    new_node = Node1(self.head, self.head.next, value)
    self.head.next = new_node
    new_node.next.prev = new_node
    self.size += 1

def pushback1(self,value):

    new_node = Node1(self.tail.prev, self.tail, value)
    self.tail.prev.next = new_node
    self.tail.prev = new_node
    self.size += 1

def popfront1(self):

    if self.size != 0:
        ret_val = self.head.next.data
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.size -= 1
        return ret_val
    else:
        return None

def popback1(self):
    if self.size != 0:
        ret_val = self.tail.prev.data
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1
        return ret_val
    else:
        return None

def printrecursive1(head):

    if head == None:
        print()
    
    print(head.data, end = ' ')
    printrecursive(head.next)