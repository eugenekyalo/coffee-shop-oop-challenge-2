import pytest
from coffee_shop_oop_challenge.lib import Order
from coffee_shop_oop_challenge.lib import Customer
from coffee_shop_oop_challenge.lib import  Coffee

def test_order_initialization():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 2.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 2.5

def test_order_customer_validation():
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order("Not a customer", coffee, 3.5)

def test_order_coffee_validation():
    customer = Customer("Bob")
    with pytest.raises(ValueError):
        Order(customer, "Not a coffee", 3.5)

def test_order_price_validation():
    customer = Customer("Charlie")
    coffee = Coffee("Cappuccino")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)  # Below minimum price
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)  # Above maximum price
    with pytest.raises(ValueError):
        Order(customer, coffee, "3.5")  # Not a float

def test_order_price_setter():
    customer = Customer("David")
    coffee = Coffee("Mocha")
    order = Order(customer, coffee, 4.0)
    with pytest.raises(ValueError):
        order.price = 0.5  # Below minimum price
    with pytest.raises(ValueError):
        order.price = 11.0  # Above maximum price
    order.price = 5.0
    assert order.price == 5.0

def test_order_customer_getter():
    customer = Customer("Eve")
    coffee = Coffee("Americano")
    order = Order(customer, coffee, 3.0)
    assert isinstance(order.customer, Customer)
    assert order.customer.name == "Eve"

def test_order_coffee_getter():
    customer = Customer("Frank")
    coffee = Coffee("Macchiato")
    order = Order(customer, coffee, 3.5)
    assert isinstance(order.coffee, Coffee)
    assert order.coffee.name == "Macchiato"