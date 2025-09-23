from abc import ABC, abstractmethod
from assignments.Assignment_three.InvalidAmountException import InvalidAmount

class DessertItem(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def get_cost(self):
        pass

    def get_name(self):
        return self.name

class Cookie(DessertItem):

    def __init__(self,name,number,price_per_dozen):
        super().__init__(name)
        if number <=0 or price_per_dozen<=0:
            raise InvalidAmount("Number of cookies or price must be greater than 0.")
        self.number = number
        self.price_per_dozen = price_per_dozen

    def get_cost(self):
        return self.number * self.price_per_dozen / 12

    def __repr__(self):
        return f"{self.name} ({self.number} pcs @ {self.price_per_dozen}/dozen) : Rs {self.get_cost():.2f}"


class Candy(DessertItem):

    def __init__(self, name, weight_grams,price_per_kg):
        super().__init__(name)
        if weight_grams<=0 or price_per_kg<=0:
            raise InvalidAmount("Weight or price must be greater than 0.")
        self.weight_grams = weight_grams
        self.price_per_kg = price_per_kg

    def get_cost(self):
        return self.weight_grams * self.price_per_kg / 1000

    def __repr__(self):
        return f"{self.name} ({self.weight_grams}g @ {self.price_per_kg}/kg) : Rs {self.get_cost():.2f}"


class Icecream(DessertItem):

    def __init__(self, name, cost):
        super().__init__(name)
        if cost <= 0:
            raise InvalidAmount("Cost must be greater than 0.")
        self.cost = cost

    def get_cost(self):
        return self.cost

    def __repr__(self):
        return f"{self.name} Icecream : Rs {self.get_cost():.2f}"

class Sundae(Icecream):

    def __init__(self, name, cost, topping_name, topping_cost):
        super().__init__(name,cost)
        if topping_cost < 0:
            raise InvalidAmount("Topping cost cannot be negative.")
        self.topping_name = topping_name
        self.topping_cost = topping_cost

    def get_cost(self):
        cost = super().get_cost()
        return cost + self.topping_cost

    def __repr__(self):
        return f"{self.name} Sundae with {self.topping_name} : Rs {self.get_cost():.2f}"