
class ArrayDeque():
 
    CAPACITY = 2

    def __init__(self):
        self.size = 0
        self.end = 0
        self.front = 0
        self.capacity = ArrayDeque.CAPACITY
        self.data = [None] * self.capacity

    
    def push_front(self, value):
        if self.size == self.capacity:
           self.resize()
        
        self.front = (self.front-1) % self.capacity
        self.data[self.front] = value
        self.size += 1


    def push_back(self, value):
        
        if self.size == self.capacity:
           self.resize()

        self.data[self.end] = value
        self.size += 1
        self.end = (self.end+1) % self.capacity

    def resize(self):

        self.capacity *= 2
        new_data = [None] * self.capacity

        if self.front < self.end:
            for i in range(self.front, self.end):
                new_data[i] = self.data[i]
        
        else:
            counter = 0
            for i in range(self.front, self.size):
                new_data[counter] = self.data[i]
                counter += 1
            
            for i in range(self.end):
                new_data[counter] = self.data[i]
                counter += 1
            
        
        self.data = new_data
        self.end = self.size
        self.front = 0


    def pop_front(self):
        ret_val =  self.data[self.front]

        self.data[self.front] = None
        self.front = (self.front+1) % self.capacity

        if ret_val != None:
            self.size -= 1
        
        return ret_val
        

    def pop_back(self):
        if self.end != 0:
            ret_val =  self.data[self.end-1]

            self.data[self.end-1] = None
            self.end = (self.end-1) % self.capacity
        else:
            ret_val = self.data[self.size-1]
            self.data[self.size-1] = None
            self.end = (self.end-1) % self.capacity

        if ret_val != None:
            self.size -= 1

        return ret_val

    
    def __str__(self):
        a_str = ''
        if self.front >= self.end:
            for i in range(self.front, self.capacity):
                a_str += str(self.data[i]) + ' '
            
            for i in range(self.end):
                a_str += str(self.data[i]) + ' '

        else:
            for i in range(self.front, self.end):
                a_str += str(self.data[i]) + ' '
        
        if self.size == 0:
            return ''
        else:
            return a_str.strip(' ')
    
    def get_size(self):
        return self.size

