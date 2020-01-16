import random



def random_insertion(size):
    a_list = [0] * size

    for i in range(size):
        a_list[i] = random.randint(1, 6)
    
    return a_list

#print(random_insertion(3))

# O(n), n er stærð listans sem er sett inn