class Customer:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address
        self.order = []
        self.running_total = 0

    def get_name(self):
        return self.name
    
    def get_phone(self):
        return self.phone
    
    def get_address(self):
        return self.address
    
    def get_order(self):
        return self.order
    
    def get_total(self):
        return self.running_total
    
    def add_order(self, dish):
        self.order.append(dish)
        self.running_total += dish.get_price()