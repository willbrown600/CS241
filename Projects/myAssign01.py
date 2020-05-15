##############################################
# Prove Assignment 01, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
##############################################

import random
from random import randint
print("Welcome to the number guessing game!")

seed_value = input("Enter random seed: ")
random.seed(seed_value)

no = False
continue_game = True


user_num = 0
#num = randint(1, 100)
while continue_game == True:
    num = randint(1, 100)
    count = 0
    while user_num != num:

        
        user_num = int(input("\nPlease enter a guess: "))
        count += 1

        if user_num < num:
            print("Higher")
        
        elif user_num > num:
            print ("Lower")
        
        else:
            print("Congratulations. You guessed it!\nIt took you",count,"guesses.")
            
            if input("\nWould you like to play again (yes/no)? ") == "no":
                continue_game = False
                print("Thank you. Goodbye.")
                
            else:
                True










