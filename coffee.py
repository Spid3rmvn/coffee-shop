class Coffee:
    """Represents a coffee item that can be ordered."""

    def __init__(self, name):
        """Initialize a new Coffee item with the given name (min 3 characters)."""
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters")

        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def add_order(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders

    def customers(self):
        unique_customers = []

        for order in self._orders:
            customer = order.customer
            if customer not in unique_customers:
                unique_customers.append(customer)

        return unique_customers

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0

        total = sum(order.price for order in self._orders)
        return total / len(self._orders)

    def __str__(self):
        return f"Coffee: {self._name} (Orders: {len(self._orders)})"
