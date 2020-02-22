
class SLL_Node:
    # THIS IMPLEMENTATION OF SINGLY-LINKED LIST NODE
    # MUST BE USED UNCHANGED, FOR TESTING PURPOSES
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        ret_str = ""
        node = self
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str
    
def is_ordered_helper(head):
    '''Checks if a singly linked list is ordered from
    lowest to highest'''

    if head == None or head.next == None:
        return True
    
    elif head.data > head.next.data:
        return False

    return is_ordered_helper(head.next)

def is_ordered(head):
    
    # Reverse and copy to check if its
    # ordered from highest to lowest
    # then reverse again
    reverse_head = reverseList(head)
    duplicate_head = duplicate(reverse_head)
    head = reverseList(reverse_head)
    
    boolean_1 = is_ordered_helper(head)
    boolean_2 = is_ordered_helper(duplicate_head)

    # If it's ordered either low-high or high-low, return True
    if boolean_1 or boolean_2:
        return True
    else:
        return False


def duplicate(head):
    '''Makes a duplicate of a singly linked list'''

    if head == None:
        return None

    return SLL_Node(head.data, duplicate(head.next))


def reverseList(head):
    '''Reverses a singly linked list'''

    if head == None or head.next == None:
        return head

    node = reverseList(head.next)
    head.next.next = head
    head.next = None
    return node

    
class DLL_Node:

    def __init__(self, prev = None, next = None, data = None):
        self.prev = prev
        self.next = next
        self.data = data


class DLL_List:
    
    def __init__(self, data = None, prev = None, next = None):
        self.head = DLL_Node()
        self.tail = DLL_Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    
    def build_list(self, lis):
        # Initialize the list
        self.head = DLL_Node()
        self.tail = DLL_Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

        for value in lis:
            self.insert(value)
    

    def insert(self, value):
        '''Inserts value in the back of the list'''

        new_node = DLL_Node(self.tail.prev, self.tail, value)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1
    
    def print(self, backwards = False):

        if backwards:
            n = self.tail
            while n.prev != self.head:
                print(n.prev.data, end = ' ')
                n = n.prev
        
        else:
            n = self.head

            while n.next != self.tail:
                print(n.next.data, end= ' ')
                n = n.next
            
        print()
    

    def contains(self, val):
        n = self.head.next
        if n != None:
            while n.next != None:
                if n.data == val:
                    return True
                n = n.next

        return False
        

# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    print("Singly-linked node example:")
    head = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5)))))
    print(str(head))

    # Tests for is ordered
    print(is_ordered(SLL_Node(1,SLL_Node(2, SLL_Node(3)))))
    print(is_ordered(SLL_Node(3, SLL_Node(2, SLL_Node(1)))))
    print(is_ordered(SLL_Node(1, SLL_Node(3, SLL_Node(2)))))
    print(is_ordered(SLL_Node(5, SLL_Node(6, SLL_Node(2)))))
    print(is_ordered(SLL_Node(5)))
    print(is_ordered(SLL_Node()))

    # Tests for dll
    my_dll = DLL_List()
    my_dll.build_list([2,6,3,6,2,8,9])
    my_dll.print()
    my_dll.print(True)
    print('6:' + str(my_dll.contains(6))+ '7:' + str(my_dll.contains(7)))

    my_dll.build_list([2,2,6])
    my_dll.print()
    my_dll.print(True)
    print('6:' + str(my_dll.contains(6))+ '7:' + str(my_dll.contains(7)))

    my_dll.build_list([1,2])
    my_dll.print()
    my_dll.print(True)
    print('6:' + str(my_dll.contains(6))+ '7:' + str(my_dll.contains(2)))