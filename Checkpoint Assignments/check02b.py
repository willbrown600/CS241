##############################################
# Checkpoint 02b, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
##############################################

def main():

    filename = prompt()

    linecount = parseLine(filename)

    wordcount = parseWord(filename)

    print("The file contains",linecount,"lines and",wordcount,"words.")

def parseLine(filename):

    count = 0
    with open(filename) as f:
        for line in f:
            #lines = line.readline()
            count = count + 1
        #print(lines)    
            
    return count
            
def parseWord(filename):

    count = 0
    with open(filename) as f:
        for line in f:
            words = line.split()
            for word in words:
                count += 1

    return count

    
    #filename.close()

def prompt():

    filename = input("Enter file: ")
    return filename

if __name__ == "__main__":
    main()





