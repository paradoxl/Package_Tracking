import csv

with open('data/packageData.csv', mode='r') as file:
    csvFile = csv.reader(file)

    for lines in csvFile:
        print(lines)

with open('data/distanceData.csv' , mode='r') as file:
    csvFile = csv.reader(file)

    for lines in csvFile:
        print(lines)