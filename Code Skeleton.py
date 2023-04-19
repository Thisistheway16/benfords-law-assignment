import matplotlib.pyplot as plt
import csv
import os

def loadData():
    while True:
        filePath = input("Enter the file path for sales data (sales (1).csv): ")
        if not os.path.isfile(filePath):
            print("Error: invalit file path. Please try again: ")
            continue
        if not filePath.endswith(".csv"):
            print("Error: invalid file extension. Please try again: ")
            continue

        salesData = []

        with open(filePath, 'r') as file:
            csvReader = csv.reader(file, delimiter = ",")
            for row in csvReader:
                salesData.append(row[1])
        print(salesData)
        return salesData
    
    
def printMenu():
    """
This function prints the menu options for the customer and sales system.
    """
    userInput = ""
    loadDataOption = "1"
    dataAnalysisOption = "2"
    exitCondition = "3"

    while userInput != exitCondition:
        print('''
===Welcome===
1. Load Data\n
2. Analyze Data (Check For Fraud)\n
3. Quit\n
        ''')
        userInput = input("> ")        

        if userInput == loadDataOption:
            loadData()
        elif userInput == dataAnalysisOption: 
            analyzeData()
        else:
            print("Please type in a valid option (A number from 1-3)")

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

    return numbers # Return the dictionary full of the keys and values. Key being the number, value being the amount of times that number shows up.

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

    return numbers # Return the dictionary full of the keys and values. Key being the number, value being the percentage that number shows up 



def isFraud():
    '''Checks if the number 1 appears at least 29%, up to 32% of the time. Returns False if so, and Yes otherwise'''

    localDictionary = salesDictionaryCount()
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

def analyzeData():
    '''Show the graph, and check for fraud'''
    showGraph(isFraud())

def showGraph(fraud = False):
    '''Shows the bar graph '''
    percent = list(salesDictionaryPercent().keys())
    number = list(salesDictionaryPercent().values())

    # Create the bar chart
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(percent, number, color='red', width=0.4)
    
    ax.text(8.7, 30, f'Fraud: {fraud}', fontsize = 8.5)
 
    plt.xlabel("Digit")
    plt.ylabel("Percent")
    plt.title("Leading Digit Distribution")
    plt.show()

printMenu()
