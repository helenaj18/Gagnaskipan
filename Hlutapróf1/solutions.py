
# Part A



def count_values(lis):

    unique_dict = {}

    for value in lis:

        if value in unique_dict:
            unique_dict[value] += 1
        else:
            unique_dict[value] = 1
    
    for key, val in unique_dict.items():

        print('{}: {}'.format(key,val))

print('\nPART A test\n')
count_values(['a','b','a','d','c','d','c','c','f','b','a','a'])



# Part B

class ValueCounter:

    def set_items(self, lis):
        self.unique_dict = {}
        
        for value in lis:

            if value in self.unique_dict:
                self.unique_dict[value] += 1
            else:
                self.unique_dict[value] = 1
        
        return self.unique_dict

    def print_count(self):

        for key, val in self.unique_dict.items():

            print('{}: {}'.format(key,val))


print('\nPART B test\n')

value_counter = ValueCounter()
value_counter.set_items(['a','b','a','d','c','d','c','c','f','b','a','a'])
value_counter.print_count()