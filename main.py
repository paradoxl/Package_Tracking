import csv
import datetime
import sys

from Package_Tracking.trucks import trucks
from hashTable import HashTable

#pull in and create trucks
firstTruck = trucks([1,13,14,15,16,20,29,30,31,34,37,40],0.0,None,datetime.timedelta(hours=8))
secondTruck = trucks([3,6,12,17,18,19,21,22,23,24,26,27,35,36,38,39],0.0,None,datetime.timedelta(hours=10,minutes=30))
thirdTruck = trucks([2,4,5,6,7,8,9,10,11,25,28,32,33], 0.0,None,datetime.timedelta(hours=9,minutes=5))

#generate packages
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

#determines the values of package status
def setStat(conv):
    if deliveredAt < conv:
        status = "Delivered"
    elif deliveredAt > conv:
        status = "On the way"
    else:
        status = "At hub"


# returns all packages
def packageList():
    with open('data/packageData.csv',mode='r',encoding='utf-8-sig') as pData:
        reader = csv.reader(pData)
        for row in reader:
            value = HT.getValue(int(row[0]))
        return value
# returns packages based on id
def searchPackageByID(ID):
    value = HT.getValue(int(ID))
    return value

# calculates distances from row col
def distanceCalc(r,c):
        with open("data/distanceData.csv", mode='r', encoding='utf-8-sig') as file:
                distance = list(csv.reader(file))
                val = distance[r][c]
                if val == '' or "":
                        val = distance[c][r]
                return  float(val)

#return addresses id
def address(val):
    with open("data/locationNames.csv",mode='r',encoding='utf-8-sig') as file:
        names = list(csv.reader(file))
        for name in names:
            if val in name[2]:
                return int(name[0])


# arranges the packages on the truck based on the most efficient route.
def load(val):
    ND = []
    for id in val.packages:
        package = HT.getValue(id)
        ND.append(package)
    val.packages.clear()

    while not len(ND):
        next = sys.maxsize
        pack = None
        for i in ND:
            if distanceCalc(address(val.address),distanceCalc(package.address)) <= next:
                next = distanceCalc(address(val.address),address(package.address))
                pack = package
        val.packages.append(pack.id)
        ND.remove(pack)
        val.distance += next
        val.address = next
        val.time += datetime.timedelta(hours=next/18)
        next.deliveryTime = val.time





load(firstTruck)