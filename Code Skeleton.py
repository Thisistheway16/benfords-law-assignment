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
    
    
    