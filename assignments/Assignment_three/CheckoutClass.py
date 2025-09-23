from assignments.Assignment_three.DessertClass import *
from assignments.Assignment_three.CartIsEmptyException import *

class Checkout:
    def __init__(self):
        self.cart = []

    def enter_item(self, item:DessertItem):
        self.cart.append(item)

    def clear(self):
        self.cart.clear()

    def number_of_items(self):
        return len(self.cart)

    def total_cost(self):
        if not self.cart:
            raise CartIsEmpty("Cart is empty! Add items before checkout.")
        return sum(item.get_cost() for item in self.cart)

    def __str__(self):
        if not self.cart:
            raise CartIsEmpty("Cart is empty! Cannot generate invoice.")
        invoice = "\n---- INVOICE ----\n"
        for item in self.cart:
            invoice += str(item) + '\n'
        invoice += f"---------------\ntotal: Rs {self.total_cost():.2f}"
        return invoice


try:
    checkout = Checkout()
    checkout.enter_item(Candy("Fudge", 200, 50))
    checkout.enter_item(Cookie("ChocoChip", 4, 10))
    checkout.enter_item(Icecream("Vanilla", 30))
    checkout.enter_item(Sundae("Chocolate", 40, "Nuts", 10))

    print(checkout)

    checkout.clear()
    print(checkout.total_cost())

except InvalidAmount as e:
    print(e)
except CartIsEmpty as e:
    print(e)
