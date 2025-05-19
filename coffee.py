class Coffee:
    def __init__(self, name):
        """
        Initialize a Coffee with a name.
        
        Args:
            name (str): Name of the coffee (at least 3 characters)
            
        Raises:
            TypeError: If name is not a string
            ValueError: If name is less than 3 characters
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters")

        self._name = name
        self._orders = []

    @property
    def name(self):
        """
        Get the coffee's name.
        
        Returns:
            str: The coffee's name
        """
        return self._name

    def add_order(self, order):
        """
        Add an order for this coffee.
        
        Args:
            order: The Order instance to add
        """
        self._orders.append(order)

    def orders(self):
        """
        Get all orders for this coffee.
        
        Returns:
            list: List of Order instances
        """
        return self._orders

    def customers(self):
        """
        Get unique list of customers who ordered this coffee.
        
        Returns:
            list: List of unique Customer instances
        """
        unique_customers = []

        for order in self._orders:
            customer = order.customer
            if customer not in unique_customers:
                unique_customers.append(customer)

        return unique_customers

    def num_orders(self):
        """
        Get the total count of orders for this coffee.
        
        Returns:
            int: Number of orders (0 if none)
        """
        return len(self._orders)

    def average_price(self):
        """
        Calculate the mean price of all orders for this coffee.
        
        Returns:
            float: Average price (0 if no orders)
        """
        if not self._orders:
            return 0

        total = sum(order.price for order in self._orders)
        return total / len(self._orders)

    def __str__(self):
        return f"Coffee: {self._name} (Orders: {len(self._orders)})"
