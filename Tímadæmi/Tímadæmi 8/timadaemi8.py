

class Stack:

    CAPACITY = 2
    def __init__(self):
        self.capacity = Stack.CAPACITY
        self.data = [0] * self.capacity
        self.size = 0
        
    def push(self, value):

        if self.size == self.capacity:
            self.resize()
        
        self.data[self.size] = value
        self.size += 1
 
    def resize(self):

        self.capacity *= 2
        new_data = [0] * self.capacity

        for i in range(self.size):
            new_data[i] = self.data[i]
        
        self.data = new_data


    def pop(self):
        ret_val = self.data[self.size-1]
        
        self.data[self.size-1] = None
        self.size -= 1

        return ret_val


    def __str__(self):

        a_str = ''
        for i in range(self.size):
            a_str += str(self.data[i]) + ', '
        
        return a_str.strip(', ')


print('STACK')
s = Stack()
s.push(5)
print(s)
s.pop()
print(s)
s.push(3)
print(s)
s.push(5)
print(s)
s.push(4)
s.push(2)
s.pop()
print(s)


class Queue:
    CAPACITY = 2

    def __init__(self):
        self.size = 0
        self.front = 0
        self.end = 0
        self.capacity = Queue.CAPACITY
        self.data = [0] * self.capacity

    
    def add(self, value):
        if self.size == self.capacity:
            self.resize()

        self.data[self.end] = value
        self.size += 1
        self.end = (self.end+1) % self.capacity

    def resize(self):

        self.capacity *= 2
        new_data = [0] * self.capacity

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


    def remove(self):
        ret_val = self.data[self.front]

        self.data[self.front] = None
        self.front = (self.front+1) % self.capacity

        self.size -= 1
    
        return ret_val
    
    def __str__(self):
        a_str = ''
        if self.front >= self.end:
            for i in range(self.front, self.capacity):
                a_str += str(self.data[i]) + ', '
            
            for i in range(self.end):
                a_str += str(self.data[i]) + ', '

        else:
            for i in range(self.front, self.end):
                a_str += str(self.data[i]) + ', '
        
        return a_str.strip(', ')


print('QUEUE')
q = Queue()
q.add(5)
print(q)
q.add(7)
print(q)
q.add(9)
print(q)
q.remove()
print(q)
q.add(4)
print(q)
q.add(2)
print(q)
q.remove()
print(q)
q.add(4)
print(q)
q.add(2)
print(q)
q.add(4)
print(q)
q.add(2)
print(q)


class Deque:

    CAPACITY = 2

    def __init__(self):
        self.size = 0
        self.end = 0
        self.front = 0
        self.capacity = Deque.CAPACITY
        self.data = [0] * self.capacity

    
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
        new_data = [0] * self.capacity

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

        self.size -= 1

        return ret_val

    def pop_back(self):
        ret_val =  self.data[self.end]

        self.data[self.end] = None

        self.end = (self.end-1) % self.capacity
        self.size -= 1

        return ret_val

    
    def __str__(self):
        a_str = ''
        if self.front >= self.end:
            for i in range(self.front, self.capacity):
                a_str += str(self.data[i]) + ', '
            
            for i in range(self.end):
                a_str += str(self.data[i]) + ', '

        else:
            for i in range(self.front, self.end):
                a_str += str(self.data[i]) + ', '
        
        return a_str.strip(', ')


print('DEQUE')

d = Deque()
d.push_back(3)
print(d)
d.push_front(4)
print(d)
d.push_back(3)
print(d)
d.pop_front()
print(d)
d.push_back(1)
print(d)
d.pop_back()
print(d)
d.push_back(3)
print(d)
d.push_front(4)
print(d)
d.push_back(3)
print(d)
d.push_front(4)
print(d)