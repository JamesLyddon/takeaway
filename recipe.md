As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

(Use the twilio-python package to implement this next one. You will need to use mocks too.)

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

```python
class Takeaway:
    def __init__(self):
        self.menu = [] # list of dishes with prices
        self.active_customers = [] # list of customers currently ordering
    
    # takeaway methods
    def add_dish_to_menu(self, name, price):
        # create dish object and add to menu
        pass

    def remove_dish_from_menu(self, name):
        # remove a dish from the menu
        pass

    def calc_total(self, items):
        # calculate total of all items ordered

    # customer methods 
    def list_dishes(self):
        # return a list of dishes with prices
        pass

    def place_order(self):
        # select some number of several available dishes
        pass

    def get_receipt(self):
        # return itemised receipt of meals ordered with prices
        pass

    def send_confirmation_txt(self):
        # confirm the order with a sms txt using twillo api and time.time to estimate delivery
        # "Thank you! Your order was placed and will be delivered before 18:52"
        pass

class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address
        self.order = []
```