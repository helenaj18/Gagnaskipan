
# Tímaflækja O(2^n)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(8))


# Tímaflækja O(n)
def fibonacci2(n):

    if n <= 1:
        return (n, 0)
    
    a, b = fibonacci2(n-1)
    return (a+b, a)

print(fibonacci2(8))