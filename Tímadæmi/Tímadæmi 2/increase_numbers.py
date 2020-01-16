import random

def increase_numbers(a_list):

    size = len(a_list)
    index = random.randint(0,size-1)
    a_list[index] += 1

    return a_list


print(increase_numbers([1,2,3,46,7]))

# O(1) því skiptir ekki máli hvað listinn er stór