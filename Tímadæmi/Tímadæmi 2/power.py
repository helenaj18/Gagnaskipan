# O(n)
def power(param1,param2):
    '''Returns param1 in the power of param2 '''
    tot = 1
    for n in range(param2):
        tot *= param1
    
    return tot

# n er stærð param2, þ.e. í hvaða veldi param1 á að vera