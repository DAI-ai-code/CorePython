from abc import ABC, abstractmethod


class DessertItem(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def get_cost(self):
        pass

    def get_name(self):
        return self.name

class Cookie(DessertItem):
    price = 100
    def __init__(self,name,quantity):
        super().__init__(name)
        self.quantity = quantity

    def get_cost(self):
        return self.quantity * Cookie.price / 12

    def __repr__(self):
        return f"Name = {self.name} Quantity = {self.quantity} total = {self.get_cost()}"


class Candy(DessertItem):
    price = 1000

    def __init__(self, name, quantity):
        super().__init__(name)
        self.quantity = quantity

    def get_cost(self):
        return self.quantity * Candy.price / 1000

    def __repr__(self):
        return f"Name = {self.name} Quantity = {self.quantity} total = {self.get_cost()}"

class Icecream(DessertItem):
    price = 50

    def __init__(self, name, quantity):
        super().__init__(name)
        self.quantity = quantity

    def get_cost(self):
        return self.quantity * Icecream.price

    def __repr__(self):
        return f"Name = {self.name}, Quantity = {self.quantity}, total = {self.get_cost()}"

class Sundae(Icecream):
    topping_price = 10

    def __init__(self, name, quantity):
        super().__init__(name,quantity)

    def get_cost(self):
        cost = super().get_cost()
        return cost + (self.quantity * Sundae.topping_price)