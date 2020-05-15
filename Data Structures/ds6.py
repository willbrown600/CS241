##############################################
# Team Activity 06, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
#
##############################################

from collections import deque

class Student:

    def __init__(self):

        self.name = ""
        self.course = ""

    def prompt(self):
        
        self.name = input("Enter name: ")
        self.course = input("Enter course: CS ")


    def display(self):

        print("Now helping {} with CS {}".format(self.name, self.course))


class HelpSystem:

    def __init__(self):

        self.waiting_list = deque()

    def is_student_waiting(self):

        if len(self.waiting_list) > 0:
            return True
        else:
            return False


    def add_to_waiting_list(self, student):

        self.waiting_list.append(student)


    def help_next_student(self):

        if self.is_student_waiting() == True:

            student = self.waiting_list.popleft()
            print()
            student.display()
            print()

        else:
            print("\nNo one to help\n")

    
def main():

    
    h = HelpSystem()

    selection = 0

    print("Options: ")
    while selection != 3:
        print("1. Add a new student")
        print("2. Help next student")
        print("3. Quit")
        selection = int(input("Enter selection: "))

        if selection == 1:

            s = Student()
            print()
            s.prompt()
            print()
            h.add_to_waiting_list(s)

        elif selection == 2:

            h.help_next_student()
            print()

    print("\nGoodbye\n")

if __name__ == "__main__":
    main()
            






