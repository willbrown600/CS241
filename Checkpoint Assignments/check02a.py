##############################################
# Checkpoint 02a, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
##############################################

def main():

    numbers = []

    numlist = prompt(numbers)

    numbers = numlist

    compute_sum(numlist)


def prompt(numbers):
    
    count = 0
    num = False
    
    while num != True:
    
        user_num = int(input("Enter a positive number: "))
        
        if user_num < 0: 
            print("Invalid entry. The number must be positive.")
            num = False
    
        else:
            count = count + 1
            if count < 4:
                print("")
                numbers.append(user_num)
                if count == 3:
                    num = True
                else:
                    num = False
                
            else:
                num = True
            
            
    return numbers

def compute_sum(numlist):

    sum = 0
    for i in range(len(numlist)):
        sum = sum + numlist[i]

    print("The sum is: " + str(sum))


if __name__ == "__main__":
    main()