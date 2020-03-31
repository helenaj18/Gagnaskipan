class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Array:
    def __init__(self):
        self.capacity = 2
        self.array = [0] * self.capacity
        self.size = 0

    def add(self, value):
        if self.size >= self.capacity:
            self.resize()
        
        self.array[self.size] = value
        self.size += 1

    def __str__(self):
        a_str = ''
        for i in range(self.size):
            a_str += str(self.array[i]) + ' '
        return a_str
    
    def __len__(self):
        return self.size
    
    def resize(self):
        self.capacity *= 2
        new_array = [0] * self.capacity

        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array


    def linear_search(self, value, start = 0):

        if start == self.size:
            raise NotFound()
        elif self.array[start] == value:
            return start
        
        return self.linear_search(value, start+1)
            
    def remove_value(self, value):

        index = self.linear_search(value)
        self.remove_at(index)

    def remove_at(self, index):

        if 0 <= index and index < self.size:
            for i in range(index, self.size-1):
                self.array[i] = self.array[i+1]

            self.array[self.size-1] = None
            self.size -= 1
        
        else:
            raise IndexOutOfBounds
            
    def remove_duplicates(self):
        
        for i in range(self.size):
            for j in range(i+1, self.size):
                if self.array[i] == self.array[j]:
                    self.remove_value(self.array[j])


# Tests

a = Array()
a.add(5)
a.add('bla')
print(a)
a.remove_duplicates()
print(a)
a.add(5)
print(a)
a.remove_duplicates()
print(a)
a.add(3)
a.add(2)
print(a)