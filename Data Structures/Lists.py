##############################################
# Data Structures: Lists, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
##############################################

oddList = []
evenList = []
user_num = 1

while (user_num != 0):

    user_num = int(input("Enter a number: "))

    if (user_num % 2 == 0):
        if (user_num != 0):
            evenList.append(user_num)
    else:
        oddList.append(user_num)

print()
print("Even numbers: ")
for number in evenList:
    print(number)
    #print()

print()
print("Odd numbers: ")
for number in oddList:
    print(number)
    print()


