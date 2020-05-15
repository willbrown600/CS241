########################################
# Prove Assignment 04, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
########################################

class Product:

    def __init__(self, id, name, price, quantity):

        self.id = id
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def get_total_price(self):

        return self.price * self.quantity


    def display(self):

        print("{} ({}) - ${:.2f}".format(self.name, self.quantity, self.get_total_price()))