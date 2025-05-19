import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from order import Order
from coffee import Coffee
from customer import Customer


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")

    def test_init(self):
        order = Order(self.customer, self.coffee, 4.50)

        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 4.50)

        with self.assertRaises(TypeError):
            Order("Not a customer", self.coffee, 4.50)

        with self.assertRaises(TypeError):
            Order(self.customer, "Not a coffee", 4.50)

        with self.assertRaises(TypeError):
            Order(self.customer, self.coffee, "Not a number")

        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.50)

        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 11.00)

    def test_customer_property(self):
        order = Order(self.customer, self.coffee, 4.50)
        self.assertEqual(order.customer, self.customer)

    def test_coffee_property(self):
        order = Order(self.customer, self.coffee, 4.50)
        self.assertEqual(order.coffee, self.coffee)

    def test_price_property(self):
        order = Order(self.customer, self.coffee, 4.50)
        self.assertEqual(order.price, 4.50)

        with self.assertRaises(AttributeError):
            order.price = 5.00

    def test_order_added_to_coffee(self):
        order = Order(self.customer, self.coffee, 4.50)
        self.assertIn(order, self.coffee.orders())


if __name__ == "__main__":
    unittest.main()
