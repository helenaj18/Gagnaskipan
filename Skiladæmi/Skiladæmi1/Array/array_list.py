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
    SIZE = 0
    def __init__(self):
        # Initializes the array
        self.capacity = ArrayList.CAPACITY
        self.array = [0] * ArrayList.CAPACITY
        self.size = ArrayList.SIZE
        self.order = True

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
        
        if self.check_valid_index(index):

            if self.size == self.capacity:
                self.resize()
            
            # Move all items after the index to the right 
            for i in range(self.size, index, -1):
                self.array[i] = self.array[i-1]
            
            self.array[index] = value

            self.size += 1

            self.ordered = False


    # Time complexity: O(1) - constant time
    def append(self, value):
        '''Adds value to the end of an array'''
        self.insert(value, self.size)

        if self.check_if_ordered():
            self.ordered = True
        else:
            self.ordered = False
    

    def check_if_ordered(self):
        '''Returns True if the array is ordered, else false'''
        for i in range(self.size-1):
            if self.array[i]>self.array[i+1]:
                return False
        
        return True

    def check_valid_index(self,index):
        '''Returns True if the index is valid,
         else raises an IndexOutofBounds'''

        if self.size < index or index < -self.size:
            raise IndexOutOfBounds()
        else:
            return True

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if self.check_valid_index(index):
            self.array[index] = value

        self.ordered = False

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.size == 0:
            raise Empty()
        else:
            return self.array[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if self.check_valid_index(index):
            return self.array[index]

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.size == 0:
            raise Empty()

        else:
            return self.array[self.size-1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        #ATH má ekki hafa *= 2
        self.capacity *= 2
        new_array = [0]*self.capacity

        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array


    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):

        if self.check_valid_index(index):
            for i in range(self.size, index, -1):
                self.array[i] = self.array[i-1]

            self.array[self.size-1] = None
            self.size -= 1

    # þarf að tékka á ef þetta er orðið mjög lítið miðað við capacity
       # if self.capacity >= 2*self.size:

            

    #Time complexity: O(1) - constant time
    def clear(self):

        for i in range(self.size, 0, -1):
            self.remove_at(i)
        

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def insert_ordered(self, value):

        if self.ordered == False:
            raise NotOrdered()
        else:
            self.append(value)

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
            return self.binary_search(self.array, value, self.size)
    
        elif not self.ordered:
            return self.linear_search(self.array, value)
        else:
            raise NotFound()
            
    def linear_search(self, a_list, value):

        if a_list == []:
            raise NotFound()
        elif a_list[0] == value:
            return 0
        
        return 1+self.linear_search(a_list[1:], value)

    def binary_search(self, a_list, value, size):

        if size == 1:
            if a_list[0] == value:
                return 0
            else:
                raise NotFound()

        mid = size//2

        if a_list[mid] == value:
            return mid
        elif value < a_list[mid]:

            return 1+self.binary_search(a_list[:mid], value, size-1)
        else:

            return mid+self.binary_search(a_list[mid:], value, size-1)        

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def remove_value(self, value):

        index = self.find(value)
        self.remove_at(index)


if __name__ == "__main__":
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    print(str(arr_lis))
    arr_lis.append(2)
    arr_lis.insert_ordered(1)
    arr_lis.append(7)
    print(str(arr_lis))
    print(arr_lis.find(7))
    arr_lis.remove_value(7)
    print(arr_lis)
    # arr_lis.prepend(3)
    # arr_lis.prepend(5)
    # arr_lis.prepend(6)
    # arr_lis.prepend(8)

    # arr_lis.insert(1,9)
    # print(str(arr_lis))
    # arr_lis.set_at(7,2)
    # print(str(arr_lis))
    # print(arr_lis.get_first())
    # print(arr_lis.get_at(1))
    # print(arr_lis.get_last())
    # arr_lis.clear()
    # print(arr_lis)

