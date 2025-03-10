# Nelson Oseguera

# April 14th, 2023

# Programming Project 9

# The program should take in the number of pints donated during the drive, based on a seven hour drive period and store the values in a list.  The average pints donated during that period should be calculated and displayed.  Additionally, the highest and the lowest number of pints donated should be determined and displayed.

# the main method

def main():

    endProgram = 'no'

    print()

    while endProgram == 'no':

        print()

        # declare variables

        pints = [0] * 7

        totalPints = 0

        averagePints = 0

        highPints = 0

        lowPints = 0

        # function calls

        pints = getPints(pints)

        totalPints = getTotal(pints, totalPints)

        averagePints = getAverage(totalPints, averagePints)

        highPints = getHigh(pints, highPints)

        lowPints = getLow(pints, lowPints)

        displayInfo(averagePints, highPints, lowPints)

        endProgram = input('Do you want to end program? (Enter no or yes): ')

        while not (endProgram == 'yes' or endProgram == 'no'):

            print('Please enter a yes or no')

            endProgram = input('Do you want to end program? (Enter no or yes): ')

# the getPints function

def getPints(pints):

    counter = 0

    while counter < 7:

        pints[counter] = input('Enter pints collected: ')

        counter = counter + 1

    return pints

# the getTotal function

def getTotal(pints, totalPints):

    counter = 0

    while counter < 7:

        totalPints = totalPints + int(pints[counter])

        counter = counter + 1

    return totalPints

# the getAverage function

def getAverage(totalPints, averagePints):

    averagePints = totalPints / 7

    return averagePints

# the getHigh function

def getHigh(pints, highPints):

    highPints = pints[0]

    counter = 1

    while counter < 7:

        if pints[counter] > highPints:

            highPints = pints[counter]

        counter = counter + 1

    return highPints

# the getLow function

def getLow(pints, lowPints):

    lowPints = pints[0]

    counter = 1

    while counter < 7:

        if pints[counter] < lowPints:

            lowPints = pints[counter]

        counter = counter + 1

    return lowPints

# the displayInfo method

def displayInfo(averagePints, highPints, lowPints):

    print('The average number of pints donated is', averagePints)

    print('The highest pints donated is', highPints)

    print('the lowest pints donated is', lowPints)

# start the program

main()
