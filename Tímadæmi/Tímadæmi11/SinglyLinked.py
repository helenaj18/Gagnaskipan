class Node:

    def __init__(self, data = None, next = None):
        self.next = next
        self.data = data


def headInsert(value, head):
    newHead = Node(value, head)
    return newHead

def printList(head):
    if head == None:
        print()
        return
    print(head.data, end=', ')
    printList(head.next)


def listLength(head):
    if head == None:
        return 0
    return 1 + listLength(head.next)


def listSum(head):
    if head == None:
        return 0
    return head.data + listSum(head.next)


def insertOrdered(head, value):

    if head == None:
        return Node(value, head)
    
    elif value < head.data:
        new_node = Node(value, head)
        return new_node
    
    else:
        head.next = insertOrdered(head.next, value)
        return head


def reverseList(head):
    if head.next == None:
        return head

    node = reverseList(head.next)
    head.next.next = head
    head.next = None
    return node


def mergeLists(head_one, head_two):

# búin að klára stökin í fyrri listanum, skila því head two
    if head_one == None:
        return head_two

    elif head_two == None:
        return head_one
    
    elif head_one.data < head_two.data:
        # held áfram í head one listanum en ekki head two því
        # er búin að setja minna stakið inn í sameiginlega listann
        head_one.next = mergeLists(head_one.next, head_two)
        return head_one # þarf að gera svona til að gera tengingarnar réttar
    
    else:
        head_two.next = mergeLists(head_one, head_two.next)
        return head_two


def mergeSort(head):
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




head = None
head = headInsert(3,head)
head = headInsert(5,head)
head = headInsert(1,head)
printList(head)
# printList(head)
# print(listLength(head))
# print(listSum(head))

# insertOrdered(head, 4)
# insertOrdered(head, 2)
# printList(head)

# new_head = reverseList(head)
# printList(new_head)


# head_two = None
# head_two = headInsert(7,head_two)
# head_two = headInsert(6,head_two)
# head_two = headInsert(4,head_two)
# printList(head_two)

# head_3 = mergeLists(head, head_two)

#printList(head_3)

head = mergeSort(head)
printList(head)