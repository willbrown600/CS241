########################################
# Checkpoint 09a, CS241
# Author: Will Brown
# Brother N.Parrish
########################################

def main():
    
    num = False
    
    while num == False:
        
        try:
            
            number = int(input("Enter a number: "))
            total = number * 2
            print("The result is: {}".format(total))
            num = True
            
        except ValueError:
            
            print("The value entered is not valid")
            num = False
            
    
                 



if __name__ == "__main__":
    main()