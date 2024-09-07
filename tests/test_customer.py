import pytest
from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

def test_customer_initialization():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")  # Empty name
    with pytest.raises(ValueError):
        Customer("ThisNameIsTooLong")  # More than 15 characters

def test_customer_name_setter():
    customer = Customer("Bob")
    customer.name = "Robert"
    assert customer.name == "Robert"
    with pytest.raises(ValueError):
        customer.name = "ThisNameIsTooLong"

def test_customer_orders():
    customer = Customer("Charlie")
    coffee = Coffee("Espresso")
    order = customer.create_order(coffee, 2.5)
    assert customer.orders() == [order]

def test_customer_coffees():
    customer = Customer("David")
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")
    customer.create_order(espresso, 2.5)
    customer.create_order(latte, 3.5)
    customer.create_order(espresso, 2.5)
    assert set(customer.coffees()) == {espresso, latte}

def test_create_order():
    customer = Customer("Eve")
    coffee = Coffee("Cappuccino")
    order = customer.create_order(coffee, 4.0)
    assert isinstance(order, Order)
    assert order in customer.orders()
    assert order in coffee.orders()

def test_most_aficionado():
    coffee = Coffee("Mocha")
    customer1 = Customer("Frank")
    customer2 = Customer("Grace")
    customer1.create_order(coffee, 4.0)
    customer2.create_order(coffee, 5.0)
    customer2.create_order(coffee, 5.0)
    assert Customer.most_aficionado(coffee) == customer2

def test_most_aficionado_no_orders():
    coffee = Coffee("Americano")
    assert Customer.most_aficionado(coffee) is None