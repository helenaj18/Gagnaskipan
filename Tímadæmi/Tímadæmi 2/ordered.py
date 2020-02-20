import random
num = random.randint(1,6)
def ordered_insert(a_list,num):

    a_list.append(num)

    # Starts at the end and goes back
    for i in range(len(a_list)-2, -1, -1):
        # If the element at index i is bigger 
        # than at index i+1, switch them
        if a_list[i] > a_list[i+1]:
            temp = a_list[i]
            a_list[i] = a_list[i+1]
            a_list[i+1] = temp
    
    return a_list


print(ordered_insert([1,2,3,5,6,8,9],num))

# Tímaflækjan er O(n) fyrir single insertion 
# en ef maður myndi inserta fyrir lista með n stökum
# væri flækjan O(n^2)