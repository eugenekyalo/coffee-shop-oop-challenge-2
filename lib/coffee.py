class Coffee:
    def __init__(self, name):
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self.name = name
        self._orders = []  # Private access for the orders list

    def add_order(self, order):
        """Adds an order to the coffee's list of orders."""
        self._orders.append(order)

    def orders(self):
        """Returns a list of all orders associated with this coffee."""
        return self._orders[:]  # Return a copy to avoid external modification

    def customers(self):
        """Returns a set of unique customers who have ordered this coffee."""
        return {order.customer for order in self._orders}

    def num_orders(self):
        """Returns the number of orders for this coffee."""
        return len(self._orders)

    def average_price(self):
        """Calculates and returns the average price of all orders for this coffee."""
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)
