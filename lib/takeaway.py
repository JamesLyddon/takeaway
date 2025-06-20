class Takeaway:
    def __init__(self):
        self.menu = [] # list of dishes with prices
        self.current_customer = None # list of customers currently ordering
    
    # takeaway methods
    def add_dish_to_menu(self, dish):
        self.menu.append(dish)

    def remove_dish_from_menu(self, name):
        self.menu = [dish for dish in self.menu if dish.get_name() != name]
    
    def add_customer(self, customer):
        self.current_customer = customer
    
    def remove_customer(self):
        self.current_customer = None
    
    # customer methods 
    def show_menu(self):
        return self.menu

    def take_order(self, string_order):
        # select some number of several available dishes
        for item in self.menu:
            if item.name in string_order:
                self.current_customer.add_order(item)

    def get_receipt(self):
        # return itemised receipt of meals ordered with prices
        receipt = ''
        for item in self.current_customer.get_order():
            receipt += f"1 x {item.name} | £{item.price:,.2f}\n"
        receipt += f"total: £{self.current_customer.get_total():,.2f}\n"
        return receipt

    def send_confirmation_txt(self):
        # confirm the order with a sms txt using twillo api and time.time to estimate delivery
        # "Thank you! Your order was placed and will be delivered before 18:52"
        pass