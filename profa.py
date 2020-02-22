def is_ordered(head):
    
    reverse_head = reverseList(head)

    duplicate_head = duplicate(reverse_head)

    head = reverseList(reverse_head)
    
    boolean_1 = is_ordered_helper(head)


    boolean_2 = is_ordered_helper(duplicate_head)

    if boolean_1 or boolean_2:

        return True
    else:
        return False