class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        self._orders = []
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        from .order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.add_order(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        coffee_customers = coffee.customers()
        if not coffee_customers:
            return None
        return max(coffee_customers, key=lambda c: sum(o.price for o in c.orders() if o.coffee == coffee))