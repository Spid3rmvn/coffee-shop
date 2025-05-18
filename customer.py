class Customer:
    """
    Represents a customer of the coffee shop.
    """

    def __init__(self, name):
        """
        Initialize a new Customer.

        Args:
            name (str): Customer's name (1-15 characters)
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        if len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be between 1 and 15 characters")

        self.name = name
        self.orders = []

    def get_coffees(self):
        """
        Get unique list of coffees ordered by this customer.
        """
        unique_coffees = []

        for order in self.orders:
            coffee = order.coffee
            if coffee not in unique_coffees:
                unique_coffees.append(coffee)

        return unique_coffees

    def create_order(self, coffee, price):
        """
        Create a new order for this customer.
        """
        # Import Order here to avoid circular imports
        from order import Order

        # Create a new order
        order = Order(self, coffee, price)

        # Add the order to this customer's orders
        self.orders.append(order)

        # Return the new order
        return order
