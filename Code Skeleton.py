def printMenu():
    """
This function prints the menu options for the customer and sales system.
    """
    print('''
          Customer and Sales System\n
          1. Enter Customer Information\n
          2. Generate Customer data file\n
          3. Report on total Sales (Not done in this part)\n
          4. Check for fraud in sales data (Not done in this part)\n
          9. Quit\n
          Enter menu option (1-9)
          ''')
    

def analyzeData():
    print("Analyzing data")


def checkForBenfordsLaw():
    numbers = { }
    amountOfLines = 0

    # Open the sales.csv file and read each line, line by line
    with open("sales.csv") as openedFile:
        for line in openedFile:

            # Get the digit to add to the dictionary
            numberToAdd = line.split(',')[1][0] # [1] represents the sales column, [0] represents the first letter of the number in the sales column 

            if numberToAdd in numbers:
                numbers[numberToAdd] += 1
            else:
                numbers[numberToAdd] = 1

        



checkForBenfordsLaw()
