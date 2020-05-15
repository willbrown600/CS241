##############################################
# Checkpoint 06b, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
#
##############################################

class Phone:

    def __init__(self):

        self.area_code = 0
        self.prefix = 0
        self.suffix = 0

    def prompt_number(self):

        #print("Phone: ")
        self.area_code = int(input("Area Code: "))
        self.prefix = int(input("Prefix: "))
        self.suffix = int(input("Suffix: "))

    def display(self):

        print("Phone info:")
        print("({}){}-{}".format(self.area_code, self.prefix, self.suffix))


class SmartPhone(Phone):

    def __init__(self):

        #super().__init__()
        self.email = ""
        

    def prompt(self):

        self.prompt_number()
        self.email = input("Email: ")

    def display(self):
        super().display()
        #self.display()
        print(self.email)


def main():

    p = Phone()
    print("Phone:")
    p.prompt_number()
    print()
    p.display()
    print()

    s = SmartPhone()
    print("Smart phone:")
    s.prompt()
    print()
    s.display()
    
    

if __name__ == "__main__":
    main()


