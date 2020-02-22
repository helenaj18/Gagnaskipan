
class Node:

    def __init__(self, prev = None, next = None, data = None):
        self.prev = prev
        self.next = next
        self.data = data


class DLL:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.curr_pos = 0
        self.curr_node = self.tail

    def __len__(self):
        return self.size
    

    def __str__(self):
        ret_str = ''
        n = self.head.next
        
        while n!= self.tail:
            ret_str += str(n.data) + ' '
            n=n.next

        return ret_str

    def insert(self, value):
        new_node = Node(self.curr_node.prev, self.curr_node, value)
        self.curr_node.prev.next = new_node
        self.curr_node.prev = new_node

        self.curr_node = new_node
        self.size +=1

    
    def remove(self):
        #if self.curr_node != None and self.curr_node.data != None:
        if self.__len__() != 0 and self.curr_pos != self.__len__()-1:
            self.curr_node.prev.next = self.curr_node.next
            self.curr_node.next.prev = self.curr_node.prev
            

            if self.curr_pos != self.__len__()-1:
                self.curr_node = self.curr_node.next
            
            else:
                self.curr_node = self.tail
                self.curr_pos = 0
            
            self.size -= 1

    
    def get_value(self):
        if self.curr_node != None:
            return self.curr_node.data
        else:
            return None


    def move_to_next(self):

        if self.curr_pos != self.__len__()-1 and self.__len__() != 0:
            self.curr_pos += 1
            self.curr_node = self.curr_node.next


    def move_to_prev(self):

        if self.curr_pos != 0 and self.curr_node != None:
            self.curr_pos -= 1
            self.curr_node = self.curr_node.prev
    

    def move_to_pos(self, position):
        if position >= 0 and position < self.__len__():
            
            if self.curr_pos < position:

                while self.curr_pos != position:
                    if self.curr_node == None:
                        self.curr_node = self.head.next.next
                    
                    self.move_to_next()

            else:

                while self.curr_pos != position:
                    self.move_to_prev()
    

    def remove_all(self, value):

        n = self.head.next
        counter = 0
        while n.next != None:

            if n.data == value:
                n.next.prev = n.prev
                n.prev.next = n.next
                if self.curr_pos == counter:
                    self.curr_pos = 0
                    self.curr_node = self.head.next
                
                self.size -= 1
                #self.curr_node = n.next
            
            n = n.next
            counter += 1

    def reverse(self):

        n = self.head

        while n != None:
            temp = n.next
            n.next = n.prev
            n.prev = temp
            n = n.prev
        
        self.head, self.tail = self.tail, self.head
        
        self.curr_pos = 0
        self.curr_node = self.head.next
    

    def sort(self):
        n = self.head.next
        if n.next != None:
            while n.next.data != None:
                if n.data > n.next.data:
                    temp = n.data
                    n.data = n.next.data
                    n.next.data = temp

                    while n.prev.data != None and n.data < n.prev.data:
                        temp = n.data
                        n.data = n.prev.data
                        n.prev.data = temp
                        n = n.prev
                        
                n = n.next

            self.curr_pos = 0
            self.curr_node = self.head.next


dll = DLL()
dll.insert(28)
dll.insert(27)
dll.insert(25)
dll.insert(25)
dll.insert(24)
dll.insert(24)
dll.insert(23)
dll.insert(22)
dll.insert(20)
dll.insert(18)
dll.insert(20)
dll.insert(12)
dll.insert(24)
dll.insert(28)
dll.insert(16)
dll.insert(11)
dll.insert(17)
dll.insert(25)
dll.insert(25)
dll.insert(24)
dll.insert(29)
dll.insert(11)
print(dll)
dll.remove_all(11)
dll.move_to_pos(21)
print(dll.curr_pos)
dll.insert(16)
print(dll.curr_pos)
print(dll)
print(dll.size)
