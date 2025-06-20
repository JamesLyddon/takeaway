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
def takeaway_empty():
    return Takeaway()

@pytest.fixture
def takeaway(dish_1, dish_2, dish_3):
    takeaway = Takeaway()
    takeaway.add_dish_to_menu(dish_1)
    takeaway.add_dish_to_menu(dish_2)
    takeaway.add_dish_to_menu(dish_3)
    return takeaway

def test_initialise(takeaway_empty):
    assert isinstance(takeaway_empty, Takeaway)
    assert takeaway_empty.menu == []
    assert takeaway_empty.current_customer == None
    
def test_add_dish_to_menu(takeaway_empty, dish_1, dish_2, dish_3):
    takeaway_empty.add_dish_to_menu(dish_1)
    takeaway_empty.add_dish_to_menu(dish_3)
    takeaway_empty.add_dish_to_menu(dish_2)
    assert takeaway_empty.show_menu() == [dish_1, dish_3, dish_2]
    
def test_remove_dish_from_menu(takeaway, dish_1, dish_2, dish_3):
    assert takeaway.show_menu() == [dish_1, dish_2, dish_3]
    takeaway.remove_dish_from_menu('orange chicken')
    assert takeaway.show_menu() == [dish_1, dish_3]
    takeaway.remove_dish_from_menu('chow mein')
    assert takeaway.show_menu() == [dish_3]
    takeaway.remove_dish_from_menu('plain rice')
    assert takeaway.show_menu() == []

def test_add_customer(takeaway, customer_1):
    takeaway.add_customer(customer_1)
    assert takeaway.current_customer == customer_1
    
def test_remove_customer(takeaway, customer_1):
    takeaway.add_customer(customer_1)
    assert takeaway.current_customer == customer_1
    takeaway.remove_customer()
    assert takeaway.current_customer is None

def test_take_order(takeaway, customer_1, dish_1, dish_2, dish_3):
    takeaway.add_customer(customer_1)
    takeaway.take_order('plain rice and chow mein')
    assert takeaway.current_customer.get_order() == [dish_1, dish_3]
    takeaway.take_order('actually an order of orange chicken too!')
    assert takeaway.current_customer.get_order() == [dish_1, dish_3, dish_2]

def test_get_total(takeaway, customer_1):
    takeaway.add_customer(customer_1)
    takeaway.take_order('plain rice and chow mein')
    assert takeaway.current_customer.get_total() == 8.00
    takeaway.take_order('actually an order of orange chicken too!')
    assert takeaway.current_customer.get_total() == 15.50

def test_receipt(takeaway, customer_1):
    takeaway.add_customer(customer_1)
    takeaway.take_order('plain rice and chow mein')
    assert takeaway.get_receipt() == ("1 x chow mein | £5.50\n1 x plain rice | £2.50\ntotal: £8.00\n")
    takeaway.take_order('actually an order of orange chicken too!')
    assert takeaway.get_receipt() == ("1 x chow mein | £5.50\n1 x plain rice | £2.50\n1 x orange chicken | £7.50\ntotal: £15.50\n")

def test_no_customer(takeaway, customer_1, customer_2):
    with pytest.raises(Exception, match="No customer added yet."):
        takeaway.remove_customer()
    with pytest.raises(Exception, match="No customer added yet."):
        takeaway.take_order('plain rice and chow mein')
    with pytest.raises(Exception, match="No customer added yet."):
        takeaway.get_receipt()
    takeaway.add_customer(customer_1)
    with pytest.raises(Exception, match="already serving a customer!"):
        takeaway.add_customer(customer_2)
    with pytest.raises(Exception, match="already serving a customer!"):
        takeaway.add_customer(customer_2)


# TODO add ability to order multiple of same dish
# TODO add texting mocking
# TODO consider __repr__ classes to aid output for ux
# TODO add functions to take input from user to view menu, take order etc. (main.py?)
# TODO add try except error handling