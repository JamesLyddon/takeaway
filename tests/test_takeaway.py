import pytest
from lib.dish import Dish
from lib.customer import Customer
from lib.takeaway import Takeaway

@pytest.fixture
def dish_1():
    return Dish('chow mein', 5.50)

@pytest.fixture
def dish_2():
    return Dish('orange chicken', 7.50)

@pytest.fixture
def dish_3():
    return Dish('plain rice', 2.50)

@pytest.fixture
def customer_1():
    return Customer('Travis', '+19876543210', {'number': '123', 'street': 'fake street', 'city': 'fake city', 'postcode': 'AA1 2BB'})


@pytest.fixture
def customer_2():
    return Customer('Bickle', '+19876543210', {'number': '245', 'street': 'faux avenue', 'city': 'faux town', 'postcode': 'BB21 2AA'})


@pytest.fixture
def takeaway():
    return Takeaway()

def test_initialise(takeaway):
    assert isinstance(takeaway, Takeaway)
    assert takeaway.menu == []
    assert takeaway.current_customer == None
    
def test_add_dish_to_menu(takeaway, dish_1, dish_2, dish_3):
    takeaway.add_dish_to_menu(dish_1)
    takeaway.add_dish_to_menu(dish_3)
    takeaway.add_dish_to_menu(dish_2)