from customer import Customer
from coffee import Coffee


class Order:
    """
    Represents a customer order at the coffee shop.
    """

    def __init__(self, customer, coffee, price):
        """
        Initialize a new Order.

        Args:
            customer (Customer): Customer placing the order
            coffee (Coffee): Coffee being ordered
            price (float): Price of the order (1.0-10.0)
        """
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")

        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance")

        self._customer = customer
        self._coffee = coffee

        if not isinstance(price, (float, int)):
            raise TypeError("price must be a number")

        price = float(price)
        if not (1.0 <= price <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0")

        self._price = price

        coffee.add_order(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    def __str__(self):
        """Return a string representation of the order."""
        return (
            f"{self._customer.name}'s order: {self._coffee.name} (${self._price:.2f})"
        )
