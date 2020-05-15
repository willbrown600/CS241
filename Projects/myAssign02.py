##############################################
# Prove Assignment 02, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
##############################################

def main():

    filename = prompt()
    print()
    
    averageComm, maxComm, minComm, maxLine, minLine = parseFile(filename)

    print("The average commercial rate is: " + str(averageComm))
    print()
    print("The highest rate is:")
    maxArray = maxLine.split(",")
    #print("{} ({}, {}) - ${}").format(maxArray[2], maxArray[0], maxArray[3], maxComm)
    #print("{} ({}, {}) - ${}").format
    print(maxArray[2], '(' + str(maxArray[0]) +', ' + str(maxArray[3]) + ') - $' + str(maxComm))
    #print(maxLine[2] 
    #print(maxComm)

    print()
    print("The lowest rate is:")
    minArray = minLine.split(",")
    print(minArray[2], '(' + str(minArray[0]) +', ' + str(minArray[3]) + ') - $' + str(minComm))
    #print(minLine)
    #print(minComm)

    #print()

    #CommRate = cRate_average(data)



def prompt():

    filename = input("Please enter the data file: ")
    return filename



def parseFile(filename):
    d = open(filename, "r")
    data = []
    average = 0
    maxComm = 0
    minComm = 1000
    lineCount = 0
    maxLine = ""
    minLine = ""

    for line in d:
        try:

            if (lineCount > 0):
                data = float(line.split(",")[6])
                average += data
                if (maxComm < data):
                    maxComm = data
                    maxLine = line
            
                if (minComm > data):
                    minComm = data
                    minLine = line
            lineCount += 1
        except:
            return "So close"

    averageComm = average / float(lineCount - 1)

    d.close()

    return averageComm, maxComm, minComm, maxLine, minLine


if __name__ == "__main__":
    main()
