class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    CAPACITY = 4
   
    def __init__(self):
        # Initializes the array
        self.capacity = ArrayList.CAPACITY
        self.array = [0] * ArrayList.CAPACITY
        self.size = 0
        self.ordered = True

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):

        return_string = ""

        for i in range(self.size):
            return_string += str(self.array[i]) + ', '
        
        return return_string.strip(', ')

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        '''Adds value into the list before the first item'''
        self.insert(value, 0)
        self.ordered = False

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        
        
        if 0<= index and index <= self.size:

            if self.size == self.capacity:
                self.resize()
            
            # Move all items after the index to the right 
            for i in range(self.size, index, -1):
                self.array[i] = self.array[i-1]
            
            self.array[index] = value

            self.size += 1

            self.ordered = False
        
        else:
            raise IndexOutOfBounds


    # Time complexity: O(1) - constant time
    def append(self, value):
        '''Adds value to the end of an array'''

        if self.size == self.capacity:
            self.resize()
        
        self.array[self.size] = value
        self.ordered = False
        self.size += 1


    #Time complexity: O(1) - constant time
    def set_at(self, value, index):

        if 0 <= index and index < self.size:
            self.array[index] = value
            self.ordered = False
        
        else:
            raise IndexOutOfBounds

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.size == 0:
            raise Empty()
        else:
            return self.array[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):

        if self.size == 0:
            raise IndexOutOfBounds

        if 0 <= index and index < self.size:
            return self.array[index]
        else:
            raise IndexOutOfBounds

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.size == 0:
            raise Empty()

        else:
            return self.array[self.size-1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        
        self.capacity *= 2
        new_array = [0]*self.capacity

        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array


    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):

        if 0 <= index and index < self.size:
            for i in range(index, self.size-1):
                self.array[i] = self.array[i+1]

            self.array[self.size-1] = None
            self.size -= 1
        
        else:
            raise IndexOutOfBounds

        # If the capacity is more than twice as 
        # big as the size, resize down
        if 2*self.size < self.capacity:
            self.resize_lower()
    
    def resize_lower(self):
        
        self.capacity = int(self.capacity/2)

        new_array = [0] * self.capacity

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
            

    #Time complexity: O(1) - constant time
    def clear(self):

        self.size = 0
        self.capacity = ArrayList.CAPACITY
        self.array = [0] * self.capacity
        self.ordered = True

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):

        if self.size == 0:
            self.ordered = True

        if self.ordered == False:
            raise NotOrdered()
        else:
            if self.capacity == self.size:
                self.resize()
            
            self.append(value)
            self.ordered = True

            # Starts at the end and goes back
            for i in range(self.size-2, -1, -1):
                # If the element at index i is bigger 
                # than at index i+1, switch them
                if self.array[i] > self.array[i+1]:
                    self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
                


    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):

        if self.ordered:
            return self.binary_search(value, 0, self.size)
    
        elif not self.ordered:
            return self.linear_search(value)

            
    #Time complexity: O(n) - linear time in size of list
    def linear_search(self, value, start = 0):


        if start == self.size:
            raise NotFound()
        elif self.array[start] == value:
            return start
        
        return self.linear_search(value, start+1)



    #Time complexity: O(log n) - logarithmic time in size of list
    def binary_search(self, value, start, end):

        if value > self.array[self.size-1]:
            raise NotFound

        if end == '':
            end = self.size

        if (end-start) == 1:
            if self.array[start] == value:
                return start
            else:
                raise NotFound()

        mid = start + (end-start)//2

        if self.array[mid] == value:
            return mid
        elif value < self.array[mid]:
            return self.binary_search(value, start, mid)
        else:
            return self.binary_search(value, mid+1, end)        


    
    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):

        index = self.find(value)
        self.remove_at(index)


if __name__ == "__main__":
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level
    pass