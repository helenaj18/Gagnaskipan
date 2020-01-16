def print_list(a_list):

    for elem in a_list[:-1]:
        print(str(elem)+ ', ',end ='')
    
    # Prenta síðasta stakið
    print(a_list[-1])

a_list = [1,25,6,7,9]
print_list(a_list)
        
# O(n), n er stærð listans