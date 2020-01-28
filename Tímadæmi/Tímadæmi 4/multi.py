# virkar bara fyrir jákvæðar
def multi(a,b):

    if a < b:
        a,b = b,a
    
    if b == 0:
        return 0
    elif a == 0:
        return 0
    

    return a + multi(a,b-1)



print(multi(2,3))