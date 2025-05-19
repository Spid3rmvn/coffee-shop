import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from coffee import Coffee
from customer import Customer

class TestCoffee(unittest.TestCase):
    
    def setUp(self):
        self.coffee = Coffee("Latte")
        self.customer1 = Customer("Alice")
        self.customer2 = Customer("Bob")
    
    def test_init(self):
        self.assertEqual(self.coffee.name, "Latte")
        self.assertEqual(len(self.coffee.orders()), 0)
        
        with self.assertRaises(TypeError):
            Coffee(123)
            
        with self.assertRaises(ValueError):
            Coffee("XY")
    
    def test_name_property(self):
        self.assertEqual(self.coffee.name, "Latte")
        
        with self.assertRaises(AttributeError):
            self.coffee.name = "Espresso"
    
    def test_orders(self):
        self.assertEqual(len(self.coffee.orders()), 0)
        
        order1 = self.customer1.create_order(self.coffee, 4.50)
        order2 = self.customer2.create_order(self.coffee, 4.75)
        
        orders = self.coffee.orders()
        self.assertEqual(len(orders), 2)
        self.assertIn(order1, orders)
        self.assertIn(order2, orders)
    
    def test_customers(self):
        self.assertEqual(len(self.coffee.customers()), 0)
        
        self.customer1.create_order(self.coffee, 4.50)
        self.customer2.create_order(self.coffee, 4.75)
        
        customers = self.coffee.customers()
        self.assertEqual(len(customers), 2)
        self.assertIn(self.customer1, customers)
        self.assertIn(self.customer2, customers)
        
        self.customer1.create_order(self.coffee, 5.00)
        
        customers = self.coffee.customers()
        self.assertEqual(len(customers), 2)
    
    def test_num_orders(self):
        self.assertEqual(self.coffee.num_orders(), 0)
        
        self.customer1.create_order(self.coffee, 4.50)
        self.customer2.create_order(self.coffee, 4.75)
        
        self.assertEqual(self.coffee.num_orders(), 2)
    
    def test_average_price(self):
        self.assertEqual(self.coffee.average_price(), 0)
        
        self.customer1.create_order(self.coffee, 4.00)
        self.customer1.create_order(self.coffee, 6.00)
        
        self.assertEqual(self.coffee.average_price(), 5.00)

if __name__ == '__main__':
    unittest.main()
