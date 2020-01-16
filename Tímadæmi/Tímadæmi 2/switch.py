import random

def switch_items():
    a_list = [2,4,6,2,5,8]
    print('Original list: ', a_list)
    size = len(a_list)
    picked_loc = random.randint(0,size-2)

    temp1 = a_list[picked_loc]
    a_list[picked_loc] = a_list[picked_loc+1]
    a_list[picked_loc+1] = temp1

    print('List after first switch: ', a_list)

    random1 = random.randint(0,size-2)
    random2 = random.randint(0,size-2)

    temp2 = a_list[random1]
    a_list[random1] = a_list[random2]
    a_list[random2] = temp2

    print('List after second switch: ', a_list)


switch_items()

# O(1) því það skiptir ekki máli hvað listinn er stór