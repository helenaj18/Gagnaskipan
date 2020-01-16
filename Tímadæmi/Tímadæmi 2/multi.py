def multi(int1, int2):
    ''' Multiplies two ints'''

    tot = 0
    # betra að plúsa stærri stærðina! 
    # ítra yfir minni
    if int1 < int2:
        temp = int1
        int1 = int2
        int2 = temp

    for n in range(int2):
        tot += int1
    
    return tot

# O(n), n er stærð á int 2

print(multi(1,5))