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
    print('''
          Customer and Sales System\n
          1. Enter Customer Information\n
          2. Generate Customer data file\n
          3. Report on total Sales (Not done in this part)\n
          4. Check for fraud in sales data (Not done in this part)\n
          9. Quit\n
          Enter menu option (1-9)
          ''')
