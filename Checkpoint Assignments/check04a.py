##############################################
# Checkpoint 04a, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
##############################################


class Person:

    def __init__(self):
        
        self.name = "anonymous"
        self.birthYear = "unknown"

    def display_Name(self):
        print("{} (b. {})".format(self.name, self.birthYear))
        #print()

class Book:

    def __init__(self):

        self.title = "untitled"
        self.author = Person()
        self.publisher = "unpublished"

    def display_BookInfo(self):

        print(self.title)
        print("Publisher:")
        print(self.publisher)
        print("Author:")
        self.author.display_Name()
        #print()

    def prompt(self):

        print("Please enter the following:")
        self.author.name = input("Name: ")
        self.author.birthYear = input("Year: ")
        self.title = input("Title: ")
        self.publisher = input("Publisher: ")
        #print()

        return self



def main():

    book = Book()

    book.display_BookInfo()
    print()

    info = book.prompt()
    print()

    book.display_BookInfo()
    #print()

    


if __name__ == "__main__":
    main()