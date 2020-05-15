##############################################
# Checkpoint 08b, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
##############################################

class GPA:

    def __init__(self):

        self._gpa = 0.0
        #self.letter = ""   

    def _set_gpa(self, _value):

        #value = self.grade
        if _value <= 0.0:
            self._gpa = 0.0

        elif _value >= 4.0:
            self._gpa = 4.0

        else:
            self._gpa = _value

    def _get_gpa(self):
    
        return self._gpa

    def _set_letter(self, letter):

        if letter == "F":
            self._gpa = 0.0
        elif letter == "D":
            self._gpa = 1.0
        elif letter == "C":
            self._gpa = 2.0
        elif letter == "B":
            self._gpa = 3.0
        else:
            self._gpa = 4.0

    def _get_letter(self):

        if self._gpa < 1.0:
            return "F"
        elif self._gpa < 2.0:
            return "D"
        elif self._gpa < 3.0:
            return "C"
        elif self._gpa < 4.0:
            return "B"
        else:
            return "A"

    gpa = property(_get_gpa, _set_gpa)

    #letter = property(_get_letter, _set_letter)

    @property
    def letter(self):
        return self._get_letter()

    """@property
    def letter.setter(self):
        self._set_letter(letter)"""

    @letter.setter
    def letter(self, letter):
        self._set_letter(letter)

    


def main():

    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))

    student._set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    student._set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

if __name__ == "__main__":
    main()