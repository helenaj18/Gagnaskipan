class Node:

    def __init__(self, prev = None, next = None, data = None):
        self.prev = prev
        self.next = next
        self.data = data

class Empty(Exception):
    pass

class DLL:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr_pos = 0
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


class DLL_Set(DLL):


    def add_value(self, value):

        if self.__contains__(value) == False:
            new_node = Node(self.head, self.head.next, value)
            
            if self.head.next != None:
                self.head.next.prev = new_node
                self.head.next = new_node
                self.size += 1
            
            else:
                self.head.next = new_node
                self.tail.prev = new_node

    def remove_value(self, value):
        n = self.head.next
        
        if n != None:
            while n.next != None:
                if n.data == value:
                    n.prev.next = n.next.next
                    n.next.prev = n.prev
                n = n.next
        
        else:
            raise Empty()


    def __contains__(self, value):
        
        n = self.head.next
        if n != None:
            while n.next != None:
                if n.data == value:
                    return True
                n = n.next

        return False

    def __str__(self):
        ret_str = ''
        n = self.head.next
        if n != None:
            while n.next!= None:
                ret_str += str(n.data) + ' '
                n=n.next
        
        else:
            ret_str = 'The set is empty'

        return ret_str
    
    # Union
    def __add__(self, other):
        new_set = DLL_Set()
        n = self.head.next
        m = other.head.next

        if n != None:
            while n.next != None:
                new_set.add_value(n.data)
                n = n.next
        
        if m != None:
            while m.next != None:
                new_set.add_value(m.data)
                m = m.next
        
        return new_set
    
    # Intersection
    def __mul__(self,other):
        new_set = DLL_Set()
        n = self.head.next

        if n != None:
            while n.next != None:
                if other.__contains__(n.data):
                    new_set.add_value(n.data)
                n = n.next
        return new_set
    
    # Difference
    def __sub__(self, other):
        
        difference = DLL_Set()
        intersection = self.__mul__(other)

        n = self.head.next

        if n != None:
            while n.next != None:
                if intersection.__contains__(n.data) == False:
                    difference.add_value(n.data)
                n = n.next
        
        return difference
    

    def subset(self, other):

        if self.__sub__(other).get_size() == 0:
            return True
        else:
            return False
        


    def __eq__(self, other):

        if self.subset(other) and other.subset(self):
            return True
        else:
            return False

dll = DLL_Set()
dll.add_value(5)
print(dll)
dll.remove_value(5)
print(dll)
dll.add_value(2)
dll.add_value(5)
dll.remove_value(2)
print(dll)

print(dll.__contains__(5))
print(dll.__contains__(7))
dll.add_value(5)
print(dll)

other = DLL_Set()
other.add_value(3)
other.add_value(5)

new = other + dll
print(new)


print('Other: ',other)
print('Dll: ', dll)

inter = other*dll
print(inter)


diff = other-dll
print(diff)

subset = dll.subset(other)
print(subset)

subset = other.subset(dll)
print(subset)

print(other == dll)


def swap(head, pos_1 = 0, pos_2 = 1):
    curr_1 = 0
    curr_2 = 0
    n = head.next

    if n != None:
        while n.next != None:
            if curr_1 == pos_1:
                temp = n.data
                temp_n = n
            
            if curr_2 == pos_2:
                temp_n.data = n.data
                n.data = temp

            curr_1 += 1
            n = n.next
            curr_2 += 1


dll.add_value(2)
dll.add_value(7)
dll.add_value(6)
dll.add_value(8)
print(dll)
swap(dll.head,0,3)
print(dll)


def insert_ordered(head, value):

    n = head.next
    new_node = Node()
    new_node.data = value
    while n.next != None:
        if n.data > value:
            n.prev.next = new_node
            new_node.next = n
            new_node.prev = n.prev
            n.prev = new_node
        
        n = n.next


new = DLL_Set()

new.add_value(5)
new.add_value(3)
new.add_value(2)

insert_ordered(new.head, 4)
print(new)


# virkar ekki eins og ég vil
def insertion_sort(head):
    
    n = head.next

    if n != None:
        
        while n.next.data != None:

            if n.data > n.next.data:
                temp = n.data
                n.data = n.next.data
                n.next.data = temp

            n = n.next

new = DLL_Set()

new.add_value(5)
new.add_value(7)
new.add_value(1)
new.add_value(4)
new.add_value(8)
print(new)
insertion_sort(new.head)
print(new)



def mergeLists(head_one, head_two):

# búin að klára stökin í fyrri listanum, skila því head two
    if head_one.next.next == None:
        return head_two

    elif head_two.next.next == None:
        return head_one
    
    elif head_one.next.data < head_two.next.data:
        # held áfram í head one listanum en ekki head two því
        # er búin að setja minna stakið inn í sameiginlega listann
        head_one = mergeLists(head_one.next, head_two)
        return head_one # þarf að gera svona til að gera tengingarnar réttar
    
    else:
        head_two.next = mergeLists(head_one, head_two.next)
        return head_two


# VITlaust sjá lausnir
def mergeSort(head):
    # remove head and tail
    # set head to first data node
    
    head = head.next
    tail.prev.next = None
    tail = tail.prev

    new_head = mergeSortHelper(head)

    # set new head and tail

    new_node = Node()

    new_head.prev = new_node
    new_node.next = new_head



def mergeSortHelper(head):

    node = head
    node_half = head

    if head == None:
        return head

    elif head.next == None:
        return head

    while node.next != None and node.next.next != None:
        node = node.next.next
        node_half = node_half.next
    else:
        node = node_half.next
        node_half.next = None
        return mergeLists(mergeSort(head), mergeSort(node))


new = DLL_Set()

new.add_value(5)
new.add_value(3)
new.add_value(2)

mergeSort(new.head)