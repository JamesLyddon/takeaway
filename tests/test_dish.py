import pytest
from lib.dish import Dish

@pytest.fixture
def dish():
    return Dish('chow mein', 5.50)

def test_initialise(dish):
    assert isinstance(dish, Dish)
    assert dish.name == 'chow mein'
    assert dish.price == 5.50

def test_get_name(dish):
    assert dish.get_name() == 'chow mein'

def test_get_price(dish):
    assert dish.get_price() == 5.50