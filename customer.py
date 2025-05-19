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
        
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order
