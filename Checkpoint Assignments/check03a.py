##############################################
# Checkpoint 03a, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
##############################################


class Student:

    def __init__(new):
        
        new.first = ""
        new.last = ""
        new.Id = 0

def prompt_student():

    student = Student()

    student.first = input("Please enter your first name: ")
    student.last = input("Please enter your last name: ")
    student.Id = input("Please enter your id number: ")

    return student


def display_student(user):

    print("\nYour information:")
    print("{} - {} {}".format(user.Id, user.first, user.last))


def main():

    user  = prompt_student()

    display_student(user)


if __name__ == "__main__":
    main()