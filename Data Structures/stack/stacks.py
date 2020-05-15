##########################################
# Data Structures: Assignment CS241
# Author: Will Brown
# Instructor: Brother N Parrish
##########################################

def read_words(file):
    my_stack = []
    #empty stack value -1 to correspond with no values
    stack_count = -1
    for line in file:
        for word in line:
        #checks for an opening bracket
            if (word == "[" or word == "{" or word == "("):
                my_stack.append(word)
                stack_count += 1
                #checking for closing bracket, if last item not closing not balanced
                # also if there is no opening bracket not balanced
            elif (word == "]" and stack_count > -1):
                if (my_stack[stack_count] != "["):
                    return "Not balanced"
                else:
                    my_stack.pop()
                    stack_count -= 1
            elif (word == "}" and stack_count > -1):
                if (my_stack[stack_count] != "{"):
                    return "Not balanced"
                else:
                    my_stack.pop()
                    stack_count -= 1
            elif (word == ")" and stack_count > -1):
                if (my_stack[stack_count] != "("):
                    return "Not balanced"
                else:
                    my_stack.pop()
                    stack_count -= 1
                #if there was a bracket but no closing bracket
            if stack_count > -1:
                return "Not balanced"
            else:
	            return "Balanced"

def prompt():

    filename = input("Please enter a filename: ")
    return filename

def main():

    file = prompt()

    read_words(file)