# Time complexity: O(n) þar sem n er stærð á veldisvísi
def power(base, exp):
    ret_val = 1
    for _ in range(exp):
        ret_val *= base

    return ret_val

# Time complexity: O(n) þar sem n er í mesta lagi lengd á listanum, minnst 0
def instert_into_list(lis, value, index):
    i = len(lis) - 1
    while i > index:
        lis[i] = lis[i-1]
        i -= 1
    lis[index] = value

list1 = [4,2,6,4,8]
print(list1)
instert_into_list(list1, 3, 2)
print(list1)

print(power(2,2))
print(power(3,2))
print(power(3,3))
print(power(2,8))


