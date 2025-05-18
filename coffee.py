class Coffee:
    """
    Represents a coffee item that can be ordered.
    """

    def __init__(self, name):
        """
        Initialize a new Coffee item.

        Args:
            name (str): Name of the coffee (at least 3 characters)
        """
        # Validate the name
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters")

        # Store the name
        self._name = name

        # Empty list to store orders
        self._orders = []

    @property
    def name(self):
        """Get the coffee's name (read-only)"""
        return self._name

    def add_order(self, order):
        """
        Add a new order for this coffee

        Args:
            order: The order to add
        """
        self._orders.append(order)

    def get_orders(self):
        """
        Get all orders for this coffee.

        Returns:
            list: All orders for this coffee
        """
        return self._orders

    def get_customers(self):
        """
        Get unique list of customers who ordered this coffee.

        Returns:
            list: Unique customers who ordered this coffee
        """
        unique_customers = []

        for order in self._orders:
            customer = order.customer
            if customer not in unique_customers:
                unique_customers.append(customer)

        return unique_customers

    def count_orders(self):
        """
        Get the total number of orders for this coffee.

        Returns:
            int: Number of orders
        """
        return len(self._orders)

    def calculate_average_price(self):
        """
        Calculate the average price of all orders for this coffee.

        Returns:
            float: Average price (0 if no orders)
        """
        if not self._orders:
            return 0

        total = 0
        for order in self._orders:
            total += order.price

        return total / len(self._orders)

    def __str__(self):
        """String representation of the coffee"""
        return f"Coffee: {self._name} (Orders: {len(self._orders)})"
