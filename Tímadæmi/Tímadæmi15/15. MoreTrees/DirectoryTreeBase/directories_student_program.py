class Node:

    def __init__(self, data = None, next = None):
        self.next = next
        self.data = data

class Linked_list:

    def __init__(self, head = None):
        self.head = head
        self.size = 0

    
    def push_front(self, value):
        new_node = Node(value, self.head)
        self.size += 1
        self.head = new_node
        
    def __str__(self):
        ret_str = ''
        n = self.head
        
        while n!= None:
            ret_str += str(n.data) + ' '
            n=n.next

        return ret_str



class TreeNode:
    def __init__(self, name = ""):
        self.name = name
        self.children = Linked_list()
        
    # ADD STUFF HERE IF NEEDED

# ADD STUFF HERE IF NEEDED

# IF YOU WANT TO PUT THIS ALL INTO A CLASS AND USE INSTANCE VARIABLES (self.xx) THAT IS OK


def run_commands_on_node(node):
    print("  current directory: " + node.name)

    while True:
        user_input = input()
        command = user_input.split()
        if command[0] == "mkdir":
            print("  Making subdirectory " + command[1])
            new_node = TreeNode(command[1])
            node.children.push_front(new_node)

        elif command[0] == "ls":
            print("  Listing the contents of current directory,  " + node.name)

            n = node.children.head
            

            while n != None:
                print(n.data.name)
                n = n.next

        elif command[0] == "cd":
            print("  switching to directory " + command[1])
                # command[1] is the name of the subdirectory that should now become the current directory
            found = False

            n = node.children.head
            
            while n != None:
                if n.data.name == command[1]:
                    run_commands_on_node(n.data)
                    found = True
                n = n.next

            if command[1] == "..":
                # "cd .." MEANS I WANT TO GO UP A FOLDER
                return # change if needed, but this should exit if you are in the root folder

            # ADD STUFF HERE IF NEEDED

            if found != True: # Change this to equivalent of "if folder not found":
                print("  No folder with that name exists")

        else:
            print("  command not recognized")

        # ADD STUFF HERE IF NEEDED



def run_directories_program():
    # YOU CAN CHANGE THE WHOLE THING IF YOU LIKE!!
    # YOU CAN DESIGN THIS DIFFERENTLY IF IT SUITS YOU
    run_commands_on_node(TreeNode("root"))

if __name__ == "__main__":
    run_directories_program()
    
