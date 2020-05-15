##############################################
# Team Activity 06, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
#
##############################################

class Point:

    def __init__(self):

        self.x = 0.0
        self.y = 0.0

    def prompt_for_point(self):

        self.x = float(input("Enter x: "))
        self.y = float(input("Enter y: "))

    def display(self):

        print("Center:")
        print("({}, {})".format(self.x, self.y))

class Circle(Point):

    def __init__(self):
        
        super().__init__()      #call the point __init__ method.
        self.radius = 0.0

    def prompt_for_circle(self):

        self.prompt_for_point()
        self.radius = float(input("Enter radius:"))

    def display(self):

        print("Center:")
        super().display()  #call from point method
        print("Radius: {}".format(self.radius))

def main():

    c = Circle()
    c.prompt_for_circle()

    print()

    c.display()

if __name__ == "__main__":
    main()
