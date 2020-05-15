########################################
# Data Structures - Dictonaries 10, CS241
# Author: Will Brown
# Brother N.Parrish
########################################

def prompt_for_numbers():
    
    numbers = []
    
    print("Enter in a list of numbers: ")
    
    num = 0
    
    while num != -1:
        num = int(input())
        
        if num != -1:
            
            numbers.append(num)
            
    return numbers


def display_numbers(numbers):
    
    for num in numbers:
        print(num)

    
    


def main():
    
    
    
    numbers = [12, 18, 128, 48, 2348, 21, 18, 3, 2, 42, 96, 11, 42, 12, 18]
    numbers.insert(0, 5)
    numbers.remove(2348)
    more_numbers = [1, 2, 3, 4, 5]
    #numbers.extend(more_numbers)
    #numbers.sort()
    #numbers.reverse()
    print(numbers.count(18))
    print(numbers.index(96))
    #print(numbers[:7])
    #print(numbers[7:])
    print(numbers)
    print(numbers[::2])
    print(numbers[::-1])
    
    
    #display_numbers(numbers)
    
    
    
    
    
if __name__ == "__main__":
    main()
    