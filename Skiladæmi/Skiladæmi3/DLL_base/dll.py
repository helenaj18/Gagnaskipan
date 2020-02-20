
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
        if self.curr_node != None and self.curr_node.data != None:
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

        if self.curr_pos != self.__len__()-1 and self.curr_node != None:
            self.curr_pos += 1
            self.curr_node = self.curr_node.next


    def move_to_prev(self):

        if self.curr_pos != 0 and self.curr_node != None:
            self.curr_pos -= 1
            self.curr_node = self.curr_node.prev
    

    def move_to_pos(self, position):
        if position > 0 and position < self.__len__():
            
            if self.curr_pos < position:

                while self.curr_pos != position:
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


print("\n\nTESTING THE BASIC STUFF\n")

dll = DLL()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("A")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("B")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("C")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("D")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("E")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_next()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_next()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("1")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("2")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_next()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("3")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("4")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_prev()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.insert("VALUE")
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_pos(8)
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))


dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.move_to_pos(2)
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
dll.remove()
print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
