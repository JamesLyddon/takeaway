import pytest
from lib.dish import Dish
from lib.customer import Customer

@pytest.fixture
def dish_1():
    return Dish('chow mein', 5.50)

@pytest.fixture
def dish_2():
    return Dish('orange chicken', 7.50)

@pytest.fixture
def customer():
    return Customer('Travis', '+19876543210', {'number': '123', 'street': 'fake street', 'city': 'fake city', 'postcode': 'AA1 2BB'})

def test_initialise(customer):
    assert isinstance(customer, Customer)
    assert customer.name == 'Travis'
    assert customer.phone == '+19876543210'
    assert customer.address == {'number': '123', 'street': 'fake street', 'city': 'fake city', 'postcode': 'AA1 2BB'}
    assert customer.address["street"] == 'fake street'

def test_get_name(customer):
    assert customer.get_name() == 'Travis'

def test_get_phone(customer):
    assert customer.get_phone() == '+19876543210'

def test_get_address(customer):
    assert customer.get_address() == {'number': '123', 'street': 'fake street', 'city': 'fake city', 'postcode': 'AA1 2BB'}
    

def test_get_order(customer):
    assert customer.get_order() == []

def test_get_total(customer):
    assert customer.get_total() == 0

def test_add_order(customer, dish_1, dish_2):
    customer.add_order(dish_1)
    assert customer.get_order() == [dish_1]
    customer.add_order(dish_2) 
    assert customer.get_order() == [dish_1, dish_2]
    
def test_get_total(customer, dish_1, dish_2):
    customer.add_order(dish_1)
    assert customer.get_total() == 5.50
    customer.add_order(dish_2)
    assert customer.get_total() == 13.00