from random import Random
# STR sem value
class Key:
    def __init__(self, int_value, str_value):
        self.i1 = int_value
        self.s = str_value

    def __eq__(self, other):
        return self.i1 == other.i1 and self.s == other.s

    def __hash__(self):
        return self.i1


if __name__ == '__main__':
    rand = Random()
    lis_size = 17
    lis = [0] * lis_size
    max_val = 0
    min_val = 12345678

    for _ in range(1000):
        key = Key(rand.randint(0,100), 'string')
        index = hash(key) % lis_size
        lis[index] += 1

    print(lis)

    for value in lis:
        if value > max_val:
            max_val = value
        
        if value < min_val:
            min_val = value
    
    difference = max_val - min_val
    ratio = difference/max_val  # vil að þetta sé sem næst núlli
    
    print(ratio)


# INT OG INT
# from random import Random

# class Key:
#     def __init__(self, int_value, int_value2):
#         self.i1 = int_value
#         self.i2 = int_value2
    
#     def __eq__(self, other):
#         return self.i1 == other.i1 and self.i2 == other.i2

#     def __hash__(self):
#         return self.i1 * self.i2


# if __name__ == '__main__':
#     rand = Random()
#     lis_size = 13
#     lis = [0] * lis_size
#     for _ in range(1000):
#         key = Key(2, rand.randint(0,100))
#         index = hash(key) % lis_size
#         lis[index] += 1
    
#     print(lis)