import random
import unittest
# Tímadæmi 2
def power(a,b):

    result = 1
    for i in range(b):
        result *= a

    return result
# O(n) þ.s. n=b

print(power(2,3))


def multi(a,b):

    if a < b:
        a,b = b,a

    result = 0
    for i in range(b):
        result += a
    
    return result


print(multi(6,4))
# O(n) þ.s. b er n


def random_(size):

    lis = [0] * size

    for i in range(size):
        lis[i] = random.randint(1,6)
    
    return lis


print(random_(5))

#O(n) og n er stærð listans


def print_list(lis):
    a_str = ''

    for elem in lis:
        a_str += str(elem) + ', '
    
    print(a_str.strip(', '))


print_list([1,5,6,6,3])
# O(n) þ.s. en eru fjöldi elementa í listanum

def increase(size):

    lis = random_(size)
    print('Upphaflegur: ',lis)

    num = random.randint(0,size-1)

    lis[num] += 1

    return lis

print(increase(5))

#O(1), skiptir ekki máli hver lengd listans er


def switch(size):
    lis = random_(size)
    print('upphaflegi: ', lis)
    # can't be at the right end
    num = random.randint(0,size-2)

    lis[num], lis[num+1] = lis[num+1],lis[num]
   
    print('Eftir fyrsta switch: ', lis)

    num1 = random.randint(0,size-1)
    num2 = random.randint(0,size-1)

    lis[num1], lis[num2] = lis[num2], lis[num1]

    print('Eftir seinna switch', lis)


switch(5)


def ordered(lis):
    num = random.randint(1,6)
    lis.append(num)

    for i in range(len(lis)-2,-1,-1):
        
        if lis[i] > lis[i+1]:
            lis[i+1], lis[i] = lis[i], lis[i+1]
    
    return lis

    #O(n)


print(ordered([5,13,14,15,30]))

def combined():

    lis = random_(7)
    lis2 = [5,13,14,15,30]

    for elem in lis:
        ordered2(lis2, elem)
    
    return lis2

#O(n^2)

def ordered2(lis,num):
    lis.append(num)

    for i in range(len(lis)-2,-1,-1):
        
        if lis[i] > lis[i+1]:
            lis[i+1], lis[i] = lis[i], lis[i+1]
    
    return lis

print(combined())


# Tímadæmi 3


class Pizza():

    def __init__(self, topping1, topping2 = '', topping3 = ''):
        self.topping1 = topping1
        self.topping2 = topping2
        self.topping3 = topping3
        self.status = 'unserved'

    
    def __str__(self):
        
        if self.topping2 == '':
            return 'Pizza: {}'.format(self.topping1)
        elif self.topping3 == '':
            return 'Pizza: {} and {}'.format(self.topping1,self.topping2)
        
        else:
            return 'Pizza: {}, {} and {}'.format(self.topping1,self.topping2,self.topping3)

class Pizzaz():

    def __init__(self):
        self.pizza_list = []

    
    def add_pizza(self,PizzaToAdd):

        if len(self.pizza_list) != 0:
            old_id, pizza = self.pizza_list[-1]
            unique_id = old_id + 1
        else:
            unique_id = 1
        return unique_id

        self.pizza_list.append((unique_id, PizzaToAdd))

        return unique_id
    
    def mark_served(self,unique_id):

        pizza = self.get_pizza(unique_id)

        pizza.status = 'served'
    
    def get_pizza(self,unique_id):
        
        for unique_id_list, pizza in self.pizza_list:
            if unique_id == unique_id_list:
                return pizza
    

    def __str__(self):
        a_str = ''

        for elem in self.pizza_list:
            a_str += str(elem)
        
        return a_str 
    

    def remove(self):

        for unique_id, pizza in self.pizza_list:
            if pizza.status == 'served':
                self.pizza_list.remove((unique_id,pizza))

            

class MyTests(unittest.TestCase):

    def TestAdd(self):

        p = Pizzaz()
        p.add_pizza(Pizza('kjot'))
        p.add_pizza(Pizza('kjot','grænt'))
        p.add_pizza(Pizza('kjot','bla','blu'))

        self.assertEqual(3, len(p.pizza_list))

    def testServed(self):

        p = Pizzaz()
        p.add_pizza(Pizza('kjot'))
        p.add_pizza(Pizza('kjot','grænt'))
        p.add_pizza(Pizza('kjot','bla','blu'))
        p.mark_served(1)
        self.assertEqual(p.get_pizza(2).status,'served')

    
    def testRemove(self):
        p = Pizzaz()
        p.add_pizza(Pizza('kjot'))
        p.add_pizza(Pizza('kjot','grænt'))
        p.add_pizza(Pizza('kjot','bla','blu'))
        p.mark_served(1)
        p.remove()

        self.assertEqual(2, len(p.pizza_list))
    

    def testPrint(self):

        p = Pizzaz()
        p.add_pizza(Pizza('kjot'))
        p.add_pizza(Pizza('kjot','grænt'))
        p.add_pizza(Pizza('kjot','bla','blu'))
        print(p)


# tester = MyTests()
# tester.TestAdd()
# tester.testServed()
# tester.testRemove()
# tester.testPrint()


# Tímadæmi 4

def power2(base,exp):

    if exp == 1:
        return base
    
    return base*power(base,exp-1)

print(power2(4,1))


def multiply(a,b):

    if a==0:
        return 0

    return b+multiply(a-1,b)

print(multiply(0,2))

def factorial(n):

    if n == 0:
        return 1
    
    return n*factorial(n-1)

print(factorial(0))


def natural(n):
    
    if n == 0:
        return 
    natural(n-1)
    print(n, end=' ')

natural(5)

def sum_of_digits(x):

    
    if len(str(x)) == 1:
        return x
    
    return x%10+sum_of_digits(x//10)

print()
print(sum_of_digits(254))


def fibonacci(n):

    if n == 1:
        return 0
    if n == 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

def fibonacci2(n):

    if n == 1:
        return (1,0)
    
    elif n == 2:
        return (1,1)
    
    a,b = fibonacci2(n-1)

    return (a+b,a)


print(fibonacci2(5))



# Tímadæmi 5

def length(a_str):

    if a_str == '':
        return 0

    return 1+length(a_str[1:])

print(length('hallo'))


def linear_search(a_list, value):

    if a_list == []:
        return False

    elif value == a_list[0]:
        return True
    
    else:
        return linear_search(a_list[1:],value)


print(linear_search([1,35,6,3,2],3))


def count_instances(a_list, value):

    if a_list == []:
        return 0

    elif value == a_list[0]:
        return 1 + count_instances(a_list[1:],value)

    else:
        return count_instances(a_list[1:],value)

print(count_instances([1,2,4,6,2],2))


def duplicates(a_list):

    if a_list == []:
        return False
    
    elif linear_search(a_list[1:],a_list[0]):
        return True
    
    else:
        return duplicates(a_list[1:])


print(duplicates([1,2,4,23,2]))


def remove_dupl(a_list):

    if not duplicates(a_list):
        return a_list
    
    elif linear_search(a_list[1:],a_list[0]):

        return remove_dupl(a_list[1:])
    
    # Appenda ekki duplicates aftast 
    
    return [a_list[0]] + remove_dupl(a_list[1:])

print(remove_dupl([1,2,4,23,2]))


def binary_search(ord_list, value):

    if ord_list == []:
        return False
    
    mid = len(ord_list)//2

    if ord_list[mid] == value:
        return True
    
    elif ord_list[mid] < value:
        return binary_search(ord_list[mid+1:], value)
    
    elif ord_list[mid] > value:
        return binary_search(ord_list[:mid], value)


print(binary_search([1,2,4,6,7,8],8))


def prefix(prefix, a_str):

    if prefix == a_str[0:len(prefix)]:
        return True
    
    
    return False


def is_substring(substring, a_str):
    
    if a_str == '':
        return False
    
    elif prefix(substring, a_str):
        return True
    
    else:
        return is_substring(substring, a_str[1:])


print(is_substring('b','gagnaskipan'))


def is_in_str(a_str, x):

    if a_str == '':
        return False

    if a_str[0] == x:
        return True
    
    return is_in_str(a_str[1:], x)
    
def x_ish(a_str, x):

    if x == '':
        return True
    
    elif is_in_str(a_str, x[0]):
        return x_ish(a_str, x[1:])
    
    return False


print(x_ish('gagnaskipan','agns'))


def palindrome_helper(forward, reversed):

    if len(forward) == 0:
        return True
    
    elif forward[0] != reversed[-1]:
        return False

    return palindrome_helper(forward[1:], reversed[:-1])

def palindrome(a_str):

    return palindrome_helper(a_str, a_str)


print(palindrome('hall'))