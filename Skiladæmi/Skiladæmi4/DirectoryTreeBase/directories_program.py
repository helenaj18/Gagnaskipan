
class TreeNode:
    def __init__(self, name = ""):
        self.name = name
        self.children = Linked_list()

class Node:

    def __init__(self, data = None, next = None):
        self.next = next
        self.data = data

class Linked_list:

    def __init__(self, head = None):
        self.head = head
        self.size = 0

    
    # def push_front(self, value):
    #     new_node = Node(value, self.head)
    #     self.size += 1
    #     self.head = new_node


    def _insert_ordered(self, value, node):

        if node == None:
            return Node(value, node)
        
        elif value.name < node.data.name:
            new_node = Node(value, node)
            return new_node
        
        else:
            node.next = self._insert_ordered(value, node.next)
            return node
    

    def remove(self, value):

        n = self.head

        while n != None:
            if n.data == value:
                n.next = n.next.next
    
    def insert_ordered(self, value):
        self.head = self._insert_ordered(value, self.head)

        
    def __contains__(self, val):
        n = self.head
        if n != None:
            while n != None:
                if n.data.name == val:
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


'''
Note that all the "if False" and "if True" are simply there to
give you the correct success and error message formats.
You can use if sentences or try catch or any other
means of programming you control flow.
You can make an encapsulting class for everything and start with that,
rather than starting with the single TreeNode("root").
Just make sure the input and output of the program is exactly as
specified and fits with the  expected_out.txt when the tester
program is run with the original commands.txt.
Then feel free to make your own, more extensive tests.
'''

def run_commands_on_tree(tree):
    print("  current directory: " + tree.name)

    while True:
        
        user_input = input()
        command = user_input.split()
        if command[0] == "mkdir":
            print("  Making subdirectory " + command[1])
                # command[1] is the name of the subdirectory that should be made here
            
            if tree.children.__contains__(command[1]):
                unique = False
            else:
                new_node = TreeNode(command[1])
                tree.children.insert_ordered(new_node)
                unique = True

            if unique == False:
                print("  Subdirectory with same name already in directory")

        elif command[0] == "ls":
            print("  Listing the contents of current directory,  " + str(tree.name)) # Add the name of the directory here
            n = tree.children.head
            
            while n != None and n.data != None:
                print(n.data.name)
                n = n.next

        elif command[0] == "cd":
            print("  switching to directory " + command[1])
            
                # command[1] is the name of the subdirectory that should now become the current directory
            found = False

            n = tree.children.head
            counter = 0
            while n != None:
                if n.data.name == command[1]:
                    run_commands_on_tree(n.data)
                    found = True
                    break
                
                counter += 1
                n = n.next

            if command[1] == "..":
                if tree.children == None:
                    print("Exiting directory program")
                return
            
            elif found == False:
                print("  No folder with that name exists")
                print("  current directory: " + tree.name)

            else:
                print("  current directory: " + tree.name)
            

        elif command[0] == "rm":
            print("  removing directory " + command[1])
                # command[1] is the name of the subdirectory that should now become the current directory
            found = False

            n = tree.children.head
            
            while n != None:
                if n.data.name == command[1]:
                    n.data = None
                    found = True
                    break
                n = n.next

            if found == True:
                print("  directory successfully removed!")
            else:
                print("  No folder with that name exists")
                print("  current directory: " + tree.name)
        else:
            print("  command not recognized")



def run_directories_program():
    # YOU CAN CHANGE THE WHOLE THING IF YOU LIKE!!
    # YOU CAN DESIGN THIS DIFFERENTLY IF IT SUITS YOU
    run_commands_on_tree(TreeNode("root"))

if __name__ == "__main__":
    run_directories_program()
    
