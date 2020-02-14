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

    str_front = getString(head)
    reverse_node = reverseList(head)
    str_back = getString(reverse_node)

    if str_front == str_back:
        return True

    return False


def reverseList(head):
    if head.next == None:
        return head

    node = reverseList(head.next)
    head.next.next = head
    head.next = None
    return node

def getString(head):
    a_str = ''
    curr = head

    while curr != None:
        a_str += str(curr.data) + ' '
        curr = curr.next
    
    return a_str.upper()


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