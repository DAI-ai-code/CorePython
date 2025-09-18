from abc import ABC, abstractmethod

class DessertItem(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_cost(self):
        pass

    def get_name(self):
        return self.name

    @abstractmethod
    def __repr__(self):
        pass

class Candy(DessertItem):
    def __init__(self, name, price, quantity):
        super().__init__(name)
        self.price = price
        self.quantity = quantity

    def get_cost(self):
        return self.price * self.quantity / 1000

    def __repr__(self):
        return f'Candy flavor: {self.name}, price = {self.price}, quantity = {self.quantity}'

class Cookie(DessertItem):

    def __init__(self, name, price, quantity):
        super().__init__(name)
        self.price = price
        self.quantity = quantity

    def get_cost(self):
        return self.price * self.quantity / 12

    def __repr__(self):
        return f'Cookie flavor: {self.name}, price = {self.price}, quantity = {self.quantity}'

class Icecream(DessertItem):
    def __init__(self, name, price, quantity):
        super().__init__(name)
        self.price = price
        self.quantity = quantity

    def get_cost(self):
        return self.price * self.quantity

    def __repr__(self):
        return f'Icecream flavor: {self.name}, price = {self.price}, quantity = {self.quantity}'

class Sundae(Icecream):
    def __init__(self, name, price, quantity, topping_name, topping_price, topping_quantity):
        super().__init__(name, price, quantity)
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.topping_quantity = topping_quantity

    def get_cost(self):
        return super().get_cost() + self.topping_price * self.topping_quantity

    def __repr__(self):
        return (f'Sundae flavor: {self.name}, price = {self.price}, quantity = {self.quantity}'
                f', topping = {self.topping_name}, topping price = {self.topping_price}, topping quantity = {self.topping_quantity}')




