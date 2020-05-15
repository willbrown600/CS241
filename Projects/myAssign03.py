##############################################
# Prove Assignment 03, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
##############################################

class Robot:

    def __init__(self):
        self.x = 10
        self.y = 10
        self.fuel = 100

    def prompt(self):
        
        #display = displayStatus()
        user = ""
        while user != "quit":
            
            user = input("Enter command: ")

            if (user == 'left'):
                if self.fuel > 0:
                    self.fuel -= 5
                    self.x -= 1
                else:
                    print("Insufficient fuel to perform action")

            elif(user == 'right'):
                if self.fuel > 0:
                    self.fuel -= 5
                    self.x += 1
                else:
                    print("Insufficient fuel to perform action")

            elif(user == 'up'):
                self.y -= 1
                if self.fuel > 0:
                    self.fuel -= 5
                else:
                    print("Insufficient fuel to perform action")

            elif(user == 'down'):
                self.y += 1
                if self.fuel > 0:
                    self.fuel -= 5
                else:
                    print("Insufficient fuel to perform action")

            elif(user == 'fire'):
                if self.fuel > 10:
                    print("Pew! Pew!")
                    self.fuel -= 15
                else:
                    print("Insufficient fuel to perform action")

            elif(user == 'status'):
                self.displayStatus()

            elif(user == 'quit'):
                print("Goodbye.")

            #print("Insufficient fuel to perform action")
                


    def displayStatus(self):
        print("({}, {}) - Fuel: {}".format(self.x, self.y, self.fuel))


def main():

    robot = Robot()
    #robot.displayStatus()
    robot.prompt()

if __name__ == "__main__":
    main()

