from desserts import *

class Checkout:

    cash_register = []

    @staticmethod
    def clear_register(self):
        Checkout.cash_register = 0

    def get_number_of_items(self):
        return len(Checkout.cash_register)

    @staticmethod
    def get_total_cost():
        total = 0
        for i in Checkout.cash_register:
            total += i.get_cost()

        Checkout.cash_register += total
        return total

    @staticmethod
    def print_cart():
        for i in Checkout.cash_register:
            print(f'{i} Total: {i.get_cost()}')

    @staticmethod
    def clear_cash_register():
        Checkout.cash_register.clear()

can = Candy("Choco candy",400,100)
cok = Cookie("Choco cookie",120,12)
ice = Icecream("Choco icecream", 50,2)
sun = Sundae("Choco icecream", 50,2,"chococococ",200,2)


Checkout.cash_register = [can, cok, ice, sun]
print(Checkout.cash_register)

# Checkout.print_cart()

Checkout.clear_cash_register()
print(Checkout.cash_register)



