class Order:
    """
    Represents a customer order at the coffee shop.
    """

    def __init__(self, customer, coffee, price):
        """
        Initialize an Order with a customer, coffee, and price.
        
        Args:
            customer: Customer instance placing the order
            coffee: Coffee instance being ordered
            price (float): Price of the order (1.0-10.0)
            
        Raises:
            TypeError: If customer is not a Customer instance
            TypeError: If coffee is not a Coffee instance
            TypeError: If price is not a number
            ValueError: If price is not between 1.0 and 10.0
        """
        from customer import Customer
        from coffee import Coffee
        
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
        
        # Add this order to the coffee's orders
        coffee.add_order(self)

      
    @property
    def customer(self):
        """
        Get the customer who placed this order.
        
        Returns:
            Customer: The customer instance
        """
        return self._customer
    
    @property
    def coffee(self):
        """
        Get the coffee that was ordered.
        
        Returns:
            Coffee: The coffee instance
        """
        return self._coffee
    
    @property
    def price(self):
        """
        Get the price of this order.
        
        Returns:
            float: The order price
        """
        return self._price

    def __str__(self):
        """Return a string representation of the order."""
        return (
            f"{self._customer.name}'s order: {self._coffee.name} (${self._price:.2f})"
        )
