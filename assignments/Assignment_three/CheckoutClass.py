from assignments.Assignment_three.DessertClass import *

class Checkout:
    def __init__(self):
        self.still_buying = True
        self.cart = {}
        self.items = 0

    def start_checkout(self):
        while self.still_buying:
            print("-"*20, "Menu", "-"*20)
            print("For Cookie press 1")
            print("For Candy press 2")
            print("For Icecream press 3")
            print("For Sundae press 4")
            print("press anything else to exit!")
            print("-"*46)

            pressed = int(input("Please press from above mentioned digits: "))

            if not 1 <= pressed <=4:
                print("You are exiting!")
                self.still_buying = False
                break
            else:
                quantity = int(input("Enter quantity: "))
                if pressed == 1:
                    c = Cookie("Choco",quantity)
                elif pressed == 2:
                    c = Candy("Strawberry",quantity)
                elif pressed == 3:
                    c = Icecream("Vanilla", quantity)
                else:
                    c = Sundae("Vanilla", quantity)

                self.items += 1
                self.cart[self.items] = c

        return self.cart

    def generate_bill(self):
        order_cart = self.cart   # use the already filled cart
        total = 0

        print("\n----- BILL SUMMARY -----")
        for key, value in order_cart.items():
            print(value)                 # __repr__ prints item details
            total += value.get_cost()    # sum cost of each item

        print("------------------------")
        print(f"TOTAL BILL: {total}")
        print("------------------------")

        return total


checkout = Checkout()
cart = checkout.start_checkout()
checkout.generate_bill()
print(cart)


