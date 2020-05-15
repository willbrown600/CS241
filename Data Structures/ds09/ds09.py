########################################
# Data Structures - Dictonaries 09, CS241
# Author: Will Brown
# Brother N.Parrish
########################################



def prompt():

    filename = input("Enter file: ")
    return filename


def parseLine(filename):

    count = 0
    with open(filename) as f:
        for line in f:
            #lines = line.readline()
            #count = count + 1
            print(line)    
            
    
            
def parseWord(filename):

    count = 0
    with open(filename) as f:
        for line in f:
            words = line.split(',')
            for word in words:
                if word[3]:
                    word.append(words)
                    count = 1
                elif word[3] > 0:
                    count += 1
        print("{} -- {}".format(count, word[3],))   
    


def display():
    
    print("{} -- {}")


def main():

    filename = prompt()

    #linecount = parseLine(filename)

    wordcount = parseWord(filename)

    #print("The file contains",linecount,"lines and",wordcount,"words.")


if __name__ == "__main__":
    main()

