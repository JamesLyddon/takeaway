class Takeaway:
    def __init__(self):
        self.menu = [] # list of dishes with prices
        self.current_customer = None # list of customers currently ordering
    
    # takeaway methods
    def add_dish_to_menu(self, name, price):
        # create dish object and add to menu
        pass

    def remove_dish_from_menu(self, name):
        # remove a dish from the menu
        pass

    def calc_total(self, items):
        # calculate total of all items ordered
        pass
    
    def add_customer(self, customer):
        # self.current_customer = customer
        pass
    
    def remove_customer(self, name):
        pass
    
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