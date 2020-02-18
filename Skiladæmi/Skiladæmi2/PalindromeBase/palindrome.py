class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def print_to_screen(head):
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")


def palindrome(head):

    reverse_head = reverseList(head)

    duplicate_head = duplicate(reverse_head)

    head = reverseList(reverse_head)

    return compare(head, duplicate_head)


def compare(head_1, head_2):

    if head_2.next == None or head_1.next == None:
        return True
    elif head_2.data == head_1.data:
        return compare(head_1.next, head_2.next)
    else:
        return False


def duplicate(head):

    if head.next == None:
        return head
    
    new_node = Node(head.data)
    new_node.next = duplicate(head.next)
    
    return new_node


def reverseList(head):
    if head.next == None:
        return head

    node = reverseList(head.next)
    head.next.next = head
    head.next = None
    return node


if __name__ == "__main__":

    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")




