##############################################
# Team Activity 06, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
#
##############################################

class Employee:

    def __init__(self):

        self.name = ""

    def display(self):

        print(self.name)

class HourlyEmployee(Employee):

    def __init__(self):

        self.hourly_wage = 0

    def display(self):

        print("{} - ${}/hour".format(self.name, self.hourly_wage))

class SalaryEmployee(Employee):

    def __init__(self):

        self.salary = 0

    def display(self):

        print("{} - ${}/year".format(self.name, self.salary))

def main():

    elist = []

    

    print("Options: ")

    selection = ""
    print("Please enter a selection.")
    print("h for hourly wage." )
    print("s for a salary.")
    print("q to quit.")

    while selection != "q" or "Q":

        n = input("Enter name: ")

        if selection == "h":
            h = int(input("Enter hourlyRate: "))
            elist.append(h)
        if selection == "s":
            s = int(input("Enter Salary: "))
            elist.append(s)

    
    print()
    print("Goodbye\n")

if __name__ == "__main__":
    main()


