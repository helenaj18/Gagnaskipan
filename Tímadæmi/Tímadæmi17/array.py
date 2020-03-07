# Gerði ekki priority hér en væri líklega svipað og í singly linked


class PriorityQueue_Array:


    CAPACITY = 4
    def __init__(self):
        # Initializes the array
        self.capacity = PriorityQueue_Array.CAPACITY
        self.array = [0] * PriorityQueue_Array.CAPACITY
        self.size = 0
    

    def insert_ordered(self, value):
        
        if self.capacity == self.size:
            self.resize()
        
        self.append(value)

        # Starts at the end and goes back
        for i in range(self.size-2, -1, -1):
            # If the element at index i is bigger 
            # than at index i+1, switch them
            if self.array[i] > self.array[i+1]:
                self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
            


    # Time complexity: O(1) - constant time
    def append(self, value):
        '''Adds value to the end of an array'''

        if self.size == self.capacity:
            self.resize()
        
        self.array[self.size] = value
        self.ordered = False
        self.size += 1
    

    def resize(self):
        
        self.capacity *= 2
        new_array = [0]*self.capacity

        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array
    

    def pop_back(self):

        ret_val = self.array[self.size-1]

        self.array[self.size-1] = 0
        self.size -= 1

        return ret_val
    

    def __str__(self):
        a_str = ''

        for i in range(self.size):
            a_str += str(self.array[i]) + ' '
        
        return a_str


p = PriorityQueue_Array()

p.insert_ordered(5)
print(p)
p.insert_ordered(3)
p.insert_ordered(6)
print(p)
p.pop_back()
print(p)