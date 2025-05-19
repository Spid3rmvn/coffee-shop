class Customer:
    """Represents a customer of the coffee shop."""

    def __init__(self, name):
        """Initialize a new Customer with a name (1-15 characters)."""
        self._name = None
        self.name = name
        self._orders = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
            
        self._name = value
    
    @property
    def orders(self):
        return self._orders
    
    def get_coffees(self):
        """Get unique list of coffees ordered by this customer."""
        unique_coffees = []
        
        for order in self._orders:
            coffee = order.coffee
            if coffee not in unique_coffees:
                unique_coffees.append(coffee)
                
        return unique_coffees
    
    def create_order(self, coffee, price):
        from order import Order
        
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order
