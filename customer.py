class Customer:
    def __init__(self, name):
        """
        Initialize a Customer with a name.
        
        Args:
            name (str): Customer's name (1-15 characters)
        """
        self._name = None
        self.name = name
        self._orders = []
    
    @property
    def name(self):
        """Get the customer's name."""
        return self._name
    
    @name.setter
    def name(self, value):
        """
        Set the customer's name.
        
        Args:
            value (str): New name (must be str, 1-15 chars)
            
        Raises:
            TypeError: If name is not a string
            ValueError: If name length is not 1-15 characters
        """
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
            
        self._name = value
    
    def orders(self):
        """
        Get all orders placed by this customer.
        
        Returns:
            list: List of Order instances
        """
        return self._orders
    
    def coffees(self):
        """
        Get unique list of coffees ordered by this customer.
        
        Returns:
            list: List of unique Coffee instances
        """
        unique_coffees = []
        
        for order in self._orders:
            coffee = order.coffee
            if coffee not in unique_coffees:
                unique_coffees.append(coffee)
                
        return unique_coffees
    
    def create_order(self, coffee, price):
        """
        Create a new order for this customer.
        
        Args:
            coffee (Coffee): The coffee being ordered
            price (float): The price of the order
        
        Returns:
            Order: The newly created order
        """
        from order import Order
        
        # Create the order
        order = Order(self, coffee, price)
        
        # Add to customer's orders
        self._orders.append(order)
        
        # Order is already added to coffee's orders in Order.__init__
        # So we don't need to call coffee.add_order(order) here
        
        return order
    
    @classmethod
    def most_aficionado(cls, coffee):
        """
        Find the customer who has spent the most money on a specific coffee.
        
        Args:
            coffee (Coffee): The coffee to check
            
        Returns:
            Customer or None: The customer who spent the most, or None if no orders exist
        """
        if not coffee.orders():
            return None
        
        # Dictionary to track total spending per customer
        customer_spending = {}
        
        for order in coffee.orders():
            customer = order.customer
            if customer not in customer_spending:
                customer_spending[customer] = 0
            customer_spending[customer] += order.price
        
        # Find the customer with the highest spending
        max_customer = None
        max_spending = 0
        
        for customer, total in customer_spending.items():
            if total > max_spending:
                max_spending = total
                max_customer = customer
        
        return max_customer
