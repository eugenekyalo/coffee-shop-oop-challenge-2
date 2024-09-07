class Order:
    def __init__(self, customer, coffee, price):
        # Validate customer, coffee, and price using property setters
        self.customer = customer  # This will trigger the validation logic in the setter
        self.coffee = coffee  # This will trigger the validation logic in the setter
        self.price = price  # This will trigger the validation logic in the setter

        # Automatically add the order to the coffee's list of orders
        coffee.add_order(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from .customer import Customer
        if not isinstance(value, Customer):
            raise ValueError("Customer must be an instance of Customer class.")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from .coffee import Coffee
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be an instance of Coffee class.")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float) or not (1.0 <= value <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        self._price = value
