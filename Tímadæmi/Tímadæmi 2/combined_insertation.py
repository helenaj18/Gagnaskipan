import random_
import ordered

def combined(size):
    a_list = random_.random_insertion(size)
    b_list = []

    for elem in a_list:
        ordered_list = ordered.ordered_insert(b_list,elem)

    return ordered_list


print(combined(5))

# Þetta er O(n^2) útaf ordered list fer n
# sinnum og elem in a list n sinnum

def combined_2(size):
    a_list = random_.random_insertion(size)

    
    for n in range(1, size):
        i = n
        temp = a_list[n]
        # i þarf að vera stærra en 0 til að það reyni ekki að færa í index sem er ekki til vinstra megin við listann
        while temp < a_list[i-1] and i > 0: 
            a_list[i] = a_list[i-1]
            a_list[i-1] = temp
            i -= 1
            

    return a_list

print(combined_2(5))

# Tímaflækjan er O(n^2) og n-ið er stærð listans

# önnur lausn

def combined_2_vol2(size):
    a_list = random_.random_insertion(size)

    cutOff = 1

    while cutOff < size:
        for i in range(cutOff, 0, -1):
            if a_list[i] < a_list[i-1]:
                temp = a_list[i]
                a_list[i] = a_list[i-1]
                a_list[i-1] = temp
            else:
                break
        cutOff += 1
    
    return a_list

print(combined_2_vol2(5))