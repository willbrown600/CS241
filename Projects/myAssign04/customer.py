########################################
# Prove Assignment 04, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
########################################

from product import Product
from order import Order

class Customer:

    def __init__(self):

        self.id = ""
        self.name = ""
        self.orders = []

    def get_order_count(self):
        count = 0
        for order in self.orders:
            count = len(self.orders)

        return count

    def get_total(self):

        total = 0
        for order in self.orders:
            total = order.get_total()

        return total

    def add_order(self, order):

        self.orders.append(order)

    def display_summary(self):

        print("Summary for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))
        print("Orders: {}".format(self.get_order_count()))
        print("Total: ${:.2f}".format(self.get_total()))
        #print()

    def display_receipts(self):

        print("Detailed receipts for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))
        print()
        for order in self.orders:
            order.display_receipt()
            
            
        
            
        
        
    
