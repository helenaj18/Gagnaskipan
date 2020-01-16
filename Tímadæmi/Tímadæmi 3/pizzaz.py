import unittest

class Pizza:

    def __init__(self, topping1, topping2 = None, topping3 = None):
        self.topping1 = topping1
        self.topping2 = topping2
        self.topping3 = topping3
        self.servedStatus = 'unserved'



class PizzaList:

    def __init__(self):
        ''' Initializes the list of pizzas'''

        self.pizza_list = []


    def create(self,PizzaToAdd):
        ''' Adds a new pizza to the pizza list'''

        self.pizza_list.append((self.get_ID(), PizzaToAdd))
        return self.get_ID()
    
    
    def get_ID(self):
        ''' Creates an id for a new pizza'''

        if len(self.pizza_list) != 0:
            old_id, pizza = self.pizza_list[-1]
            id = old_id + 1
        else:
            id = 1
        return id


    def serve(self, pizza_id):
        '''Changes the served status to served'''

        pizza = self.getPizza(pizza_id)
        if pizza:
            pizza.servedStatus = 'served'

    
    def removeServed(self):
        '''Removes all served pizzas from pizza list '''

        for id, pizza in self.pizza_list:
            if pizza.servedStatus == 'served':
                self.pizza_list.remove((id, pizza))
    

    def getPizza(self, pizza_id):
        ''' Gets an instance of class Pizza from a pizza id'''

        for id, pizza in self.pizza_list:
            if pizza_id == id:
                return pizza


    def __str__(self):
        a_str = ''
        for id, pizza in self.pizza_list:
            
            # 3 toppings
            if pizza.topping2 != None and pizza.topping3 != None:
                a_str += 'Pizza Number {}: {}, {}, {}\n'.format(id, pizza.topping1, pizza.topping2, pizza.topping3)

            # 1 topping
            elif pizza.topping2 == None and pizza.topping3 == None:
                a_str += 'Pizza Number {}: {}\n'.format(id, pizza.topping1)

            # 2 toppings
            elif pizza.topping3 == None:
                a_str += 'Pizza Number {}: {}, {}\n'.format(id, pizza.topping1, pizza.topping2)
                

        return a_str

    
class MyTest(unittest.TestCase):

    def createTest(self):
        '''Tests the create function'''

        p = PizzaList()
        p.create(Pizza('alegg1','alegg2'))
        self.assertEqual(1, len(p.pizza_list))
    

    def serveTest(self):
        '''Tests the serve function'''

        p = PizzaList()
        p.create(Pizza('alegg1','alegg2','alegg3'))
        p.create(Pizza('alegg1','alegg2','alegg3'))
        p.create(Pizza('alegg1','alegg2','alegg3'))
        p.serve(2)
        self.assertEqual(p.getPizza(2).servedStatus,'served')
    

    def removeTest(self):
        '''Tests the remove function'''
        
        p = PizzaList()
        p.create(Pizza('alegg1','alegg2','alegg3'))
        p.serve(1)
        p.removeServed()
        self.assertEqual(0, len(p.pizza_list))
    

    def testPrint(self):
        '''Tests the print function'''

        p = PizzaList()
        p.create(Pizza('alegg1'))
        self.assertEqual(str(p), 'Pizza Number 1: alegg1\n')


tester = MyTest()
tester.createTest()
tester.serveTest()
tester.removeTest()
tester.testPrint()