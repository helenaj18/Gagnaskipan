class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class Node:

    def __init__(self, data = None, next = None):
        self.next = next
        self.data = data

class Bucket:

    def __init__(self, head = None, next = None):
        self.head = head
        self.size = 0

    
    def insert(self, key, data):
        if self.contains(key):
            raise ItemExistsException()
        else:
            self.push_front((key, data))


    def push_front(self, a_tuple):
        new_node = Node(a_tuple, self.head)
        self.size += 1
        self.head = new_node
    

    def update(self, key, data):
        n = self.head

        while n!= None:
            if n.data[0] == key:
                key, value = n.data
                value = data
                n.data = (key, value)
                return
            n = n.next
        
        else:
            raise NotFoundException()
    
    def find(self, key):

        n = self.head

        while n != None:
            if n.data[0] == key:
                return n.data[1]
            n = n.next
        
        else:
            raise NotFoundException()
    
    def remove(self, key):
        n = self.head
        if n.data[0] == key:
            self.head = self.head.next
            self.size -= 1
            return

        else:
            while n.next != None:
                if n.next.data[0] == key:
                    n.next = n.next.next
                    self.size -= 1
                    return
                n = n.next
        
        raise NotFoundException()


    def __setitem__(self, key, data):
        if self.contains(key):
            return self.update(key,data)
        else:
            return self.insert(key,data)

    def __getitem__(self, key):
        return self.find(key)
    
    def __len__(self):
        return self.size

    def contains(self, key):
        '''Returns True if the bucket 
        contains the key, else False'''

        n = self.head
        while n != None:
            if n.data[0] == key:
                return True
            n = n.next

        return False
    
    def __str__(self):
        ret_str = ''
        n = self.head
        
        while n!= None:
            ret_str += str(n.data) + ' '
            n=n.next

        return ret_str


class HashMap:

    def __init__(self):
        self.lis_size = 2
        self.bucket_list = [Bucket() for _ in range(self.lis_size)]
        self.size = 0

    def rebuild(self):
        self.lis_size *= 2
        new_list = [Bucket() for _ in range(self.lis_size)]

        for bucket in self.bucket_list:
            n = bucket.head
            while n != None:
                index = self.compression(n.data[0])
                bucket = new_list[index]
                bucket.insert(n.data[0], n.data[1])
                n = n.next
        
        self.bucket_list = new_list

    def compression(self, key):
        index = hash(key) % self.lis_size
        return index


    def insert(self, key, value):
        if self.size > 1.2*self.lis_size:
            self.rebuild()

        index = self.compression(key)
        self.bucket_list[index].insert(key,value)
        self.size += 1

    def contains(self, key):
        index = self.compression(key)
        return self.bucket_list[index].contains(key)


    def find(self, key):
        index = self.compression(key)
        return self.bucket_list[index].find(key)

    def update(self, key, value):
        index = self.compression(key)
        return self.bucket_list[index].update(key,value)

    
    def remove(self, key):
        index = self.compression(key)
        return self.bucket_list[index].remove(key)



    def __setitem__(self, key, value):
        index = self.compression(key)
        return self.bucket_list[index].__setitem__(key, value)


    def __len__(self):
        size = 0
        for bucket in self.bucket_list:
            size += bucket.__len__()
        return size
    
    def __getitem__(self, key):
        index = self.compression(key)
        return self.bucket_list[index].__getitem__(key)
    

    def __str__(self):
        a_str = ''
        for bucket in self.bucket_list:
            a_str += bucket.__str__()
        
        return a_str
