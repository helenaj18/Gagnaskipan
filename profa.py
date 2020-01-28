def foo(a_str, n):
    if n == 0:
        return 0
    n -= 1
    if a_str[n] == 'a':
        return 1 + foo(a_str, n)
    return foo(a_str, n)


foo('ba',1)