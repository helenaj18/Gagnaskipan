def bar(n, m):
    if m == 0:
        return 1
    return n * bar(n, m-1)


print(bar(2,3))