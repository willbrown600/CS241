########################################
# Prove Assignment 04, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
########################################

from product import Product

class Order:

    def __init__(self):

        self.id = ""
        #self.products = Product()
        self.products = []

    def get_subtotal(self):

        total = 0
        for product in self.products:
            total += product.get_total_price()
        
        return total


    def get_tax(self):

        return 0.065 * self.get_subtotal()



    def get_total(self):

        return self.get_tax() + self.get_subtotal()


    def add_product(self, product):

        self.products.append(product)

    def display_receipt(self):

        print("Order: {}".format(self.id))
        #p = Product()
        for product in self.products:
            product.display()
        print("Subtotal: ${:.2f}".format(self.get_subtotal()))
        print("Tax: ${:.2f}".format(self.get_tax()))
        print("Total: ${:.2f}".format(self.get_total()))
    



