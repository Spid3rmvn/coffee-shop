import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee1 = Coffee("Latte")
        self.coffee2 = Coffee("Espresso")
    
    def test_init(self):
        self.assertEqual(self.customer.name, "Alice")
        self.assertEqual(len(self.customer.orders()), 0)
    
    def test_name_property(self):
        self.assertEqual(self.customer.name, "Alice")
        
        self.customer.name = "Bob"
        self.assertEqual(self.customer.name, "Bob")
        
        with self.assertRaises(TypeError):
            self.customer.name = 123
            
        with self.assertRaises(ValueError):
            self.customer.name = ""
            
        with self.assertRaises(ValueError):
            self.customer.name = "ThisNameIsTooLong"
    
    def test_orders(self):
        self.assertEqual(len(self.customer.orders()), 0)
        
        order = self.customer.create_order(self.coffee1, 4.50)
        
        orders = self.customer.orders()
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0], order)
    
    def test_coffees(self):
        self.assertEqual(len(self.customer.coffees()), 0)
        
        self.customer.create_order(self.coffee1, 4.50)
        self.customer.create_order(self.coffee2, 3.50)
        
        coffees = self.customer.coffees()
        self.assertEqual(len(coffees), 2)
        self.assertIn(self.coffee1, coffees)
        self.assertIn(self.coffee2, coffees)
        
        self.customer.create_order(self.coffee1, 4.75)
        
        coffees = self.customer.coffees()
        self.assertEqual(len(coffees), 2)
    
    def test_create_order(self):
        order = self.customer.create_order(self.coffee1, 4.50)
        
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee1)
        self.assertEqual(order.price, 4.50)
        
        self.assertIn(order, self.customer.orders())
        self.assertIn(order, self.coffee1.orders())
        
        with self.assertRaises(TypeError):
            self.customer.create_order("Not a coffee", 4.50)
            
        with self.assertRaises(ValueError):
            self.customer.create_order(self.coffee1, 0.50)

if __name__ == '__main__':
    unittest.main()
