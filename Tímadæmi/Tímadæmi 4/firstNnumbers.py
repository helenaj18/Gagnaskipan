def natural(n):

    if n < 1:
        return

    natural(n-1)
    print(n, end= ' ')


natural(5)