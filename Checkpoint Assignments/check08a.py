##############################################
# Checkpoint 08a, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
##############################################

class GPA:

    def __init__(self):

        self.gpa = 0.0
        self.letter = ""   

    def set_gpa(self, value):

        #value = self.grade
        if self.gpa < 0:
            self.gpa = 0

        elif self.gpa > 4:
            self.gpa = 4

        else:
            self.gpa = value

    def get_gpa(self):
    
        return self.gpa

    def set_letter(self, letter):

        if letter == "F":
            self.gpa = 0.0
        elif letter == "D":
            self.gpa = 1.0
        elif letter == "C":
            self.gpa = 2.0
        elif letter == "B":
            self.gpa = 3.0
        else:
            self.gpa = 4.0

    def get_letter(self):

        if self.gpa < 1.0:
            return "F"
        elif self.gpa < 2.0:
            return "D"
        elif self.gpa < 3.0:
            return "C"
        elif self.gpa < 4.0:
            return "B"
        else:
            return "A"


def main():

    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

if __name__ == "__main__":
    main()