
# Implement helper classes here
class TreeNode:
    def __init__(self, data = None, left = None, right = None, center = None):
        self.data = data
        self.left = left
        self.right = right
        self.center = center


class LRCMap:
    def __init__(self, build = False):
        if build:
            self.build_tree(TreeNode())
        else:
            self.root = TreeNode()

    def put_data(self, key, data):
        self.root = self._put_data(key, data, self.root)

    def _put_data(self, key, data, node, length = 0):
        
        if length == len(key):
            node.data = data

        if key[length:length+1] == 'l':
            if node.left == None:
                node.left = TreeNode()
            node.left = self._put_data(key, data, node.left, length+1)

        elif key[length: length+1] == 'r':
            if node.right == None:
                node.right = TreeNode()
            node.right = self._put_data(key, data, node.right, length+1)

        elif key[length: length+1] == 'c':
            if node.center == None:
                node.center = TreeNode()
            node.center = self._put_data(key, data, node.center, length+1)

        return node

    def get_data(self, key): # returns data for that key or None if non-existant
        return self._get_data(key, self.root)


    def _get_data(self, key, node, length = 0):
        if length == len(key):
            return node.data
        
        if node == None:
            return
        
        if key[length:length+1] == 'l':
            return self._get_data(key, node.left, length+1)
        elif key[length: length+1] == 'r':
            return self._get_data(key, node.right, length+1)
        elif key[length:length+1] == 'c':
            return self._get_data(key, node.center, length+1)

    def build_tree(self, node):
        self.root = self._build_tree(TreeNode())

    def _build_tree(self, node, height = 0):
        # strings of length 8 have height 8
        if height == 8:
            return TreeNode()
        
        node.left = self._build_tree(TreeNode(), height+1)
        node.center = self._build_tree(TreeNode(), height+1)
        node.right = self._build_tree(TreeNode(), height+1)
        
        return node


class HashMap:
    def __init__(self):
        self.array_length = 16
        # MUST USE ONE OF THE FOLLOWING LINES, BUT NOT BOTH
        self.hash_table = [ [ ] for _ in range(self.array_length) ]
       # self.hash_table = [ { } for _ in range(self.array_length) ]
        self.item_count = 0

    def __setitem__(self, key, data): # overrides/updates if already there
        i = 0
        index = hash(key) % self.array_length
        a_list = self.hash_table[index]

        for tuples in a_list:
            if key == tuples[0]:
                a_list[i] = (key, data)
                break
            i += 1
        else:
            a_list.append((key, data))
            self.item_count += 1

    def __getitem__(self, key): # returns data - returns None if nothing there
        index = hash(key) % self.array_length
        a_list = self.hash_table[index]

        if a_list != []:
            for key_in_list, data_in_list in a_list:
                if key_in_list == key:
                    return data_in_list
        
        return None


    def __len__(self):
        return self.item_count


# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    tm = LRCMap()
    tm.put_data("lrl", "THIS IS THE DATA FOR KEY lrl")
    tm.put_data("lc", "THIS IS THE DATA FOR KEY lc")
    print(tm.get_data("lrl"))
    print(tm.get_data("lrcclc"))
    print(tm.get_data("lc"))

    tm = LRCMap(True)
    tm.put_data("lrlrccr", "THIS IS THE DATA FOR KEY lrlrccr")
    tm.put_data("lrlrcclc", "THIS IS THE DATA FOR KEY lrlrcclc")
    print(tm.get_data("lrlrcclc"))
    print(tm.get_data("lrlclc"))
    print(tm.get_data("lrlrccr"))


    hm = HashMap()
    hm["key_value:345"] = "THIS IS THE DATA FOR KEY: key_value:345"
    hm[345] = "THIS IS THE DATA FOR KEY: 345"
    print(hm[345])
    print(hm[346])
    print(hm["key_value:345"])
    print(len(hm))
    hm[345] = "THIS IS THE NEW DATA FOR KEY: 345"
    print(hm[345])
    print(len(hm))
