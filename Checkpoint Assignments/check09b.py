########################################
# Checkpoint 09b, CS241
# Author: Will Brown
# Brother N.Parrish
########################################


def get_inverse(value):
    
    total = 1 / value
    
    if total < 0:
        print("Error: The value cannot be negative")
    else:
        print("The result is: {}".format(total))
    
def main():
        
    try:
        number = float(input("Enter a number: "))
        total = get_inverse(number)
        #print("The result is: {}".format(total))
        
    except ValueError:
        print("Error: The value must be a number")
        
            
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        
        
    except NegativeNumber:
        print("Error: The value cannot be negative")
        
        
        
if __name__ == "__main__":
    main()