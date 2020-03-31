from random import Random
class MyHashableKey:

    def __init__(self, int_value, string_value):
        self.int_value = int_value
        self.string_value = string_value
    
    def __eq__(self, other):
        return self.int_value == other.int_value and self.string_value == other.string_value

    def __hash__(self):
        ans = 0
        for letter in self.string_value:
            ans += ord(letter)
        return ans+self.int_value

