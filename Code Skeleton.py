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

        print("[!] Your data has been loaded")
        return salesData
   
def printMenu():
    """
This function prints the menu options for the customer and sales system.
    """
    userInput = ""
    loadDataOption = "1"
    checkForFraud = "2"
    dataAnalysisOption = "3"
    exportDataOption = "4"
    exitCondition = "5"

    fileData = ""

    while userInput != exitCondition:
        print('''
===Welcome===
1. Load Data\n
2. Check for Fraud\n
3. Analyze Data (Show Graphs)\n
4. Export Data\n
5. Quit\n
        ''')

        userInput = input("> ")        

        # Each function here takes in fileData as a parameter. This allows those functions to work with the File Data that the user inputs. If theres no data, it throws an error.

        if fileData == "" and userInput != loadDataOption and userInput != exitCondition:
           # Check if fileData is equal empty, meaning, the user didn't set a file path yet
           # We check if userInput isnt exitCondition so the message below doesn't show when we are trying to exit the program
            print("Seems like you havn't set a path to read yet! Use option 1 to set the file data to read from!") 
        elif userInput == loadDataOption: # If user wants to set the path 
            fileData = loadData()
        else: 
            # If the user did set a file path
            if userInput == checkForFraud:
                showIfFraud(fileData)
            elif userInput == dataAnalysisOption: 
                analyzeData(fileData)
            elif userInput == exportDataOption:
                exportData(fileData)
            else:
                print("Please type in a valid option (A number from 1-5)") # Invalid selection

def salesDictionaryCount(dataToRead):
    '''Takes in an array of the sales numbers data. Returns a dictionary of leading numbers of the dataToRead. The key is the number we are reading, and value is the amount of times that number shows up in the dataset'''
    numbers = { "1": 0,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0,
                "6": 0,
                "7": 0,
                "8": 0,
                "9": 0}

    for number in dataToRead:
         # Get the digit to add to the dictionary
        numberToAdd = number[0] # [0] represents the first letter of the number in the sales column 

        if numberToAdd in numbers:
            numbers[numberToAdd] += 1

    return numbers

def salesDictionaryPercent(dataToRead):
    '''Takes in dataToRead as an array. Returns a dictionary based on the array containing numbers 1 through 9 as the keys, and their values are the percentage that it appears'''

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

    for item in salesDictionaryCount(dataToRead):
        # Add all numbers together
        totalNumberCount += salesDictionaryCount(dataToRead)[item] # Total the numbers together


    # Divide each number by the total amount of numbers (and multiply by 100) to get the percentage
    for item in numbers:
        numbers[item] = salesDictionaryCount(dataToRead)[item] / totalNumberCount * 100 # Add result to list 

    return numbers # Return the dictionary full of the keys and values. Key being the number, value being the percentage that number shows up 

def showIfFraud(dataToRead):
    if isFraud(dataToRead):
        print("[!] This dataset is likely to be FRAUD [!]")
    else:
        print("[!] This dataset is likely to NOT be FRAUD [!]")

    print("Click enter to go back...")
    input()


def isFraud(dataToRead):
    '''Takes in dataToRead as an array. Checks if the number 1 appears at least 29%, up to 32% of the time in its leading numbers. Returns False if so, and Yes otherwise'''

    localDictionary = salesDictionaryCount(dataToRead)
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

def showGraph(dataToRead, fraud = False):
    '''Takes in an array as data to read, shows the bar graph based on the data'''
    percent = list(salesDictionaryPercent(dataToRead).keys())
    number = list(salesDictionaryPercent(dataToRead).values())

    # Create the bar chart
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(percent, number, color='red', width=0.4)
    
    ax.text(8.7, 30, f'Fraud: {fraud}', fontsize = 8.5)
 
    plt.xlabel("Digit")
    plt.ylabel("Percent")
    plt.title("Leading Digit Distribution")
    plt.show()

def analyzeData(dataToRead):
    '''Show the graph, and check for fraud'''
    showGraph(dataToRead, isFraud(dataToRead))

def exportData(dataToRead):
    '''Creates a csv file named results.csv that contains an overview of the data'''

    dict = salesDictionaryPercent(dataToRead) # Get the dictionary of data to read
    output = ""
    for number in dict: # For each number, add a new line with its information
        output += f"{number}: {round(dict[number], 1)}%\n"

    f = open(f"{os.path.abspath(os.getcwd())}/results.csv", "w") 
    f.write(output) # Write the file 
    f.close()

    print("Your file has been created!")
    print("Click enter to go back...")
    input()


printMenu()
