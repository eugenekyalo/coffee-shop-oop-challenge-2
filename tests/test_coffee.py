import pytest
from lib.coffee import Coffee
from lib.customer import Customer
from lib.order import Order

def test_coffee_initialization():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("Es")

def test_coffee_orders():
    coffee = Coffee("Latte")
    customer = Customer("Alice")
    order = Order(customer, coffee, 3.5)
    assert coffee.orders() == [order]

def test_coffee_customers():
    coffee = Coffee("Cappuccino")
    customer1 = Customer("Bob")
    customer2 = Customer("Charlie")
    Order(customer1, coffee, 4.0)
    Order(customer2, coffee, 4.5)
    assert set(coffee.customers()) == {customer1, customer2}

def test_coffee_num_orders():
    coffee = Coffee("Americano")
    customer = Customer("David")
    Order(customer, coffee, 3.0)
    Order(customer, coffee, 3.0)
    assert coffee.num_orders() == 2

def test_coffee_average_price():
    coffee = Coffee("Mocha")
    customer = Customer("Eve")
    Order(customer, coffee, 4.0)
    Order(customer, coffee, 5.0)
    assert coffee.average_price() == 4.5

def test_coffee_average_price_no_orders():
    coffee = Coffee("Macchiato")
    assert coffee.average_price() == 0