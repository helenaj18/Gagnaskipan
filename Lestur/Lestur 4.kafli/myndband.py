def foo_recur(n):
    if n < 0:
        return
    
    print(n)
    foo_recur(n-1)



foo_recur(2)


def foo_recur2(n):
    if n < 0:
        return
    
    foo_recur2(n-1)
    print(n)



foo_recur2(2)