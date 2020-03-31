n = 1000000
i = 1

# log(n)
counter = 0
while (i<n):
    i *= 2
    counter += 1

print(counter)

# n

for j in range(n):
    print(j)



# nlog(n)

# n þessi ytri
for j in range(n):
    print(j)
    i = 1
    counter = 0

    #log(n) er innri
    while (i < n):
        i *= 2
        counter += 1


# n^2, ytri er n og innri er n
for bla in range(n):
    print(bla)
    for bla in range(n):
        var = 1+1


# n^3, ysta er n, miðjan er n og innsta er n
for bla in range(n):
    print(bla)
    for bla in range(n):
        var = 1+1
        for bla in range(n):
            var2 = 2+2


# 2^n, kalla í fallið inní fallinu
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return
    
    return fib(n-1) + fib(n-2)
