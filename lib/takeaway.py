class Takeaway:
    def __init__(self):
        self.menu = [] # list of dishes with prices
        self.current_customer = None # list of customers currently ordering
    
    # helper methods
    def check_customer(self):
        if self.current_customer is None:
            raise ValueError("No customer added yet.")
    
    # takeaway methods
    def add_dish_to_menu(self, dish):
        self.menu.append(dish)

    def remove_dish_from_menu(self, name):
        self.menu = [dish for dish in self.menu if dish.get_name() != name]
    
    def add_customer(self, customer):
        if self.current_customer is None:
            self.current_customer = customer
        else:
            raise Exception("already serving a customer!")
    
    def remove_customer(self):
        self.check_customer()
        self.current_customer = None

    # customer methods 
    def show_menu(self):
        return self.menu

    def take_order(self, string_order):
        self.check_customer()
        for item in self.menu:
            if item.name in string_order:
                self.current_customer.add_order(item)

    def get_receipt(self):
        self.check_customer()
        receipt = ''
        for item in self.current_customer.get_order():
            receipt += f"{str(item)}\n"
        receipt += f"total: £{self.current_customer.get_total():,.2f}\n"
        return receipt

    def send_confirmation_txt(self):
        # confirm the order with a sms txt using twillo api and time.time to estimate delivery
        # "Thank you! Your order was placed and will be delivered before 18:52"
        pass