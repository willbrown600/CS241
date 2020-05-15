"""Song Class File"""

from collections import deque

class Song:

    def __init__(self):

        self.title = "None"
        self.artist = "None"
        

    def prompt(self):

        self.title = input("Enter the title: ")
        self.artist = input("Enter the artist: ")

    
    def display(self):

        print("Playing song:")
        print("{} by {}".format(self.title, self.artist))

    

