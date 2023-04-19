def salesAnalasis():
    import csv

    with open("sales (1).csv", 'r') as file: #opens the csv file
     csvreader = csv.reader(file)# Reads the csv File
    for row in csvreader:
        print(row[1], end = '\t')#prints the second collumn and prints it in rows