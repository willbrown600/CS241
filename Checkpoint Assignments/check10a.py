########################################
# Checkpoint 10a, CS241
# Author: Will Brown
# Brother N.Parrish
########################################

"""
File: sorting.py
Original Author: Br. Burton, designed to be completed by others.
Sorts a list of numbers.
"""

def sort(numbers):
    
    """
    Fill in this method to sort the list of numbers
    """
    for index in range(len(numbers)-1, 0, -1):
        highestNumberposition = 0
        for i in range(1,index + 1):
            if numbers[i] > numbers[highestNumberposition]:
                highestNumberposition = i

        temp = numbers[index]
        numbers[index] = numbers[highestNumberposition]
        numbers[highestNumberposition] = temp

def prompt_for_numbers():
    """
    Prompts the user for a list of numbers and returns it.
    :return: The list of numbers.
    """

    numbers = []
    print("Enter a series of numbers, with -1 to quit")

    num = 0

    while num != -1:
        num = int(input())

        if num != -1:
            numbers.append(num)

    return numbers

def display(numbers):
    """
    Displays the numbers in the list
    """
    print("The list is:")
    for num in numbers:
        print(num)

def main():
    """
    Tests the sorting process
    """
    numbers = prompt_for_numbers()
    sort(numbers)
    display(numbers)

if __name__ == "__main__":
    main()