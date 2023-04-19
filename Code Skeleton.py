import matplotlib.pyplot as plt

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


def salesDictionaryCount():
    '''Returns a dictionary containing numbers 1 through 9 as the keys, and their values are the amount of time each number appears'''
    numbers = { "1": 0,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0,
                "6": 0,
                "7": 0,
                "8": 0,
                "9": 0}

    # Open the sales.csv file and read each line, line by line
    with open("sales.csv") as openedFile:
        for line in openedFile:

            # Get the digit to add to the dictionary
            numberToAdd = line.split(',')[1][0] # [1] represents the sales column, [0] represents the first letter of the number in the sales column 

            if numberToAdd in numbers:
                numbers[numberToAdd] += 1

    return numbers # Return the dictionary full of the keys and values

def salesDictionaryPercent():
    '''Returns a dictionary containing numbers 1 through 9 as the keys, and their values are the percentage that it appears'''

    # Declare new dictionary that contains the percentage rather than literal count
    numbers = { "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0}

    totalNumberCount = 0

    for item in salesDictionaryCount():
        # Add all numbers together
        totalNumberCount += salesDictionaryCount()[item] # Total the numbers together


    # Divide each number by the total amount of numbers (and multiply by 100) to get the percentage
    for item in numbers:
        numbers[item] = salesDictionaryCount()[item] / totalNumberCount * 100 # Add result to list 

    return numbers



def isFraud(localDictionary):
    '''Takes in a Dictionary and checks if the number 1 appears at least 29%, up to 32% of the time. Returns False if so, and Yes otherwise'''

    totalAmountOfNumbers = 0 # Represents the total amount of actual sales there are
    amountOfTimesOneAppeared = localDictionary['1']

    
    for item in localDictionary:
        # Add all numbers together
        totalAmountOfNumbers += localDictionary[item]

    # Divide the amount of times 1 appeared by the total amount of numbers for the percentage that 1 appeared
    percentageOfTimesOneAppeared = amountOfTimesOneAppeared / totalAmountOfNumbers

    # Check if the amount of times one appeared is between 0.29 and 0.32. If it is, return FALSE, as its likely not fraud. IF it doesn't, return TRUE as it likely is fraud
    if 0.29 <= percentageOfTimesOneAppeared <= 0.32:
        return False
    else:
        return True

def checkForFraud():
    '''Show the graph, and check for fraud'''
    showGraph()

def showGraph():
    percent = list(salesDictionaryPercent().keys())
    number = list(salesDictionaryPercent().values())

    fig = plt.figure(figsize = (10, 5))
 
    # creating the bar plot
    plt.bar(percent, number, color ='red',
            width = 0.4)
 
    plt.xlabel("Digit")
    plt.ylabel("Percent")
    plt.title("Check for fraud")
    plt.show()
