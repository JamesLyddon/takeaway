class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def __eq__(self, other):
        if not isinstance(other, Dish):
            return False
        return self.name == other.name and self.price == other.price

    def __repr__(self):
        return f"Dish(name={self.name!r}, price={self.price})"
    
    def __str__(self):
        return f"1 x {self.name} | £{self.price:,.2f}"