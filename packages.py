import csv
from hashTable import HashTable
truckOne = [] #leaves asap
truckTwo = [] #levas at 1030
truckThree = [] #contains remaining packages. Truck one will drive this after completion.

with open("data/packageData.csv",mode='r',encoding='utf-8-sig') as file:
    HT = HashTable()
    reader = csv.reader(file)
    #pull data in to variables Time Complexity: O(n)
    for row in reader:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        deadline = row[5]
        kilo = row[6]
        notes = row[7]
        start = ''
        location = ''
        status = 'at hub'
        deliveredAt = '{0:02.0f}:{1:02.0f}'.format(00,00,00)
        #assemble variables into package object
        package = [id,address,city,state,zip,deadline,kilo,notes,start,location,status,deliveredAt]
        HT.set(int(id),package)

def setTimes(conv):
    if deliveredAt < conv:
        status = "Delivered"
    elif deliveredAt > conv:
        status = "On the way"
    else:
        status = "At hub"


def packageList():
    with open('data/packageData.csv',mode='r',encoding='utf-8-sig') as pData:
        reader = csv.reader(pData)
        for row in reader:
            value = HT.getValue(int(row[0]))
        return value
def searchPackageByID(ID):
    value = HT.getValue(int(ID))
    return value