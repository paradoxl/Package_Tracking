import csv
import datetime
import sys

import packages
from packages import packagesClass
from trucks import trucks
from hashTable import HashTable

HT = HashTable()
#pull in and create trucks
#Time complexity O(1)
firstTruck = trucks([1,13,14,15,16,20,29,30,31,34,37,40],0.0,datetime.timedelta(hours=8),'4001 South 700 East')
secondTruck = trucks([3,6,12,17,18,19,21,22,23,24,26,27,35,36,38,39],0.0,datetime.timedelta(hours=9,minutes=5),'4001 South 700 East')
thirdTruck = trucks([2,4,5,7,8,9,10,11,25,28,32,33], 0.0,datetime.timedelta(hours=9,minutes=5),'4001 South 700 East')
print()
with open('data/packageData.csv',mode='r',encoding='utf-8-sig') as packageObjectData:
    p = list(csv.reader(packageObjectData))
    for package in p:
        id = int(package[0])
        address = package[1]
        city = package[2]
        state = package[3]
        zip = package[4]
        deadline = package[5]
        kilo = package[6]
        notes = package[7]
        start = package[8]
        location = package[9]
        status = package[10]
        deliveredAt = package[11]

        packageObject = packagesClass(id,address,city,state,zip,deadline,kilo,notes,start,location,status,deliveredAt)
        HT.set(id,packageObject)

#determines the values of package status
#Time complexity O(n)
def setStat(conv):
    if deliveredAt < conv:
        status = "Delivered"
    elif deliveredAt > conv:
        status = "On the way"
    else:
        status = "At hub"


# returns all packages
# Time complexity O(n)
# def packageList():
#     with open('data/packageData.csv',mode='r',encoding='utf-8-sig') as pData:
#         reader = csv.reader(pData)
#         for row in reader:
#             value = PL.getValue(int(row[0]))
#             print(value)
# returns packages based on id
# Time complexity O(1)
def searchPackageByID(ID):
    value = HT.getValue(int(ID))
    return value

# calculates distances from row col
# Time complexity O(n^2)
def distanceCalc(r,c):
    with open('data/distanceData.csv',mode='r',encoding='utf-8-sig') as dist:
        distance = 0
        distances = list(csv.reader(dist))
        for i in range(27):
            for j in range(27):
                if distances[i][j] == '' or "":
                    distances[i][j] = float(distances[j][i])
                else:
                    distances[i][j] = float(distances[i][j])
                if i == r:
                    if j == c:
                        distance = distances[i][j]
        return distance






#return addresses id
#Time Complexity O(n)
def address(val):
    with open("data/locationNames.csv",mode='r',encoding='utf-8-sig') as file:
        names = list(csv.reader(file))
        for name in names:
            if val == name[2]:
                return int(name[0])


# arranges the packages on the truck based on the most efficient route.
# This algorithm utilizes the nearest neighbor approach. The objective is to
# organize packages in the most efficient matter possible within the truck.
# I have added packages to the truck in the objects at the top. This function will take
# those packages and sort them based on the most efficient route to drop them off.
# The first for loop will generate a list of packages that are marked not delivered.
# The logic following this will then place each package back on the truck in a manner that will provided the lowest
# drive time.

# once packages are loaded onto the truck we can then calculate the distance traveled based on the distances from
# each package address. 
def load(val):

    ND = []
    for packageID in val.packages:
        packages = HT.getValue(packageID)
        ND.append(packages)
        print(packages.status)
    val.packages.clear()
    while len(ND) > 0:
        newAddress = float(sys.maxsize)
        newPackage = None
        for packages in ND:
            if distanceCalc((int(address(val.address))), int(address(packages.address))) <= newAddress:
                newAddress = distanceCalc(address(val.address),address(packages.address))
                newPackage = packages
        val.packages.append(newPackage)
        ND.remove(newPackage)
        val.distanceTraveled += newAddress
        val.address = newPackage.address
        val.time += datetime.timedelta(hours=newAddress / 18)
        newPackage.deliveredAt = val.time
        # newPackage.status = 'Delivered'




def runRoute():
    load(firstTruck)
    thirdTruck.time = secondTruck.time
    load(secondTruck)
    load(thirdTruck)
    print("Total distance Traveled:", firstTruck.distanceTraveled + secondTruck.distanceTraveled + thirdTruck.distanceTraveled)
    print("First truck returned to hub:",firstTruck.time)
    print("Second truck returned to hub:",secondTruck.time)
    print("Third truck returned to hub:",thirdTruck.time)



menu = input("Welcome! Please select a menu item below."'\n' "1: only distance and end times" '\n'"2: Search all packages"'\n' "3: Search specific package"'\n')

if int(menu) == 1:
    runRoute()

if int(menu) == 2:
    runRoute()
    for i in range(41):
        print(HT.getValue(i))
if int(menu) == 3:
    timeSearch = input("Please enter the time you wish to see in HH:MM:SS")
    (h, m, s) = timeSearch.split(":")
    timeSearchSplit = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    runRoute()
    for i in range(41):
        val = HT.getValue(int(i))

