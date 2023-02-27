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
firstTruck = trucks([1,13,14,15,16,20,29,30,31,34,37,40,25],0.0,datetime.timedelta(hours=8),'4001 South 700 East',datetime.timedelta(hours=8))
secondTruck = trucks([3,6,12,17,18,19,21,22,23,24,26,27,35,36,38,39],0.0,datetime.timedelta(hours=9,minutes=5),'4001 South 700 East',datetime.timedelta(hours=9,minutes=5))
thirdTruck = trucks([2,4,5,7,8,9,10,11,28,32,33], 0.0,datetime.timedelta(hours=10,minutes=24),'4001 South 700 East',datetime.timedelta(hours=10,minutes=24))
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

    stagingPackages = []
    for packageID in val.packages:
        packages = HT.getValue(packageID)
        stagingPackages.append(packages)
    val.packages.clear()
    while len(stagingPackages) > 0:
        newAddress = float(sys.maxsize)
        newPackage = None
        for packages in stagingPackages:
            #retruns each truck to the hub
            if len(stagingPackages) == 1:
                toHub = distanceCalc(int(address(val.address)), int(0))
                val.time += datetime.timedelta(hours=toHub / 18)
            #checks that the address for package nine is changed. The truck with
            #this package does not leave until after the correct address is identified. So the time factor is not required.
            if packages.id == 9:
                packages.address = "410 S State St"
            if distanceCalc((int(address(val.address))), int(address(packages.address))) <= newAddress:
                newAddress = distanceCalc(address(val.address),address(packages.address))
                newPackage = packages
        val.packages.append(newPackage)
        stagingPackages.remove(newPackage)
        val.distanceTraveled += newAddress
        val.address = newPackage.address
        val.time += datetime.timedelta(hours=newAddress / 18)
        newPackage.start = val.statTime
        newPackage.deliveredAt = val.time





#all three trucks are returned to the hub. We could leave two in the world but hey...Realism
load(firstTruck)
load(secondTruck)
load(thirdTruck)

print("Total distance Traveled:", firstTruck.distanceTraveled + secondTruck.distanceTraveled + thirdTruck.distanceTraveled)
print("First truck returned to hub:",firstTruck.time)
print("Second truck returned to hub:",secondTruck.time)
print("Third truck returned to hub:",thirdTruck.time)



menu = input("Welcome! Please select a menu item below."'\n' "1: All packages" '\n'"2: Search specific package packages"'\n' "3: Search all packages based on time"'\n' "4: Search Specific Package based on time"'\n')

if int(menu) == 1:
    print("Computing:")
    for i in range(1,41):
        val = HT.getValue(i)
        val.status = "Delivered"
        print(val)
if int(menu) == 2:
    val = input("Please enter the ID of the package you are looking for")
    packageVal = HT.getValue(int(val))
    packageVal.status = "Delivered"
    print(packageVal)
if int(menu) == 3:
    timeSearchOne = input("Please enter the start time you wish to see in HH:MM:SS"'\n')
    (h, m, s) = timeSearchOne.split(":")
    timeSearchSplit = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    timeSearchTwo = input("Please enter the end time you wish to see in HH:MM:SS"'\n')
    (h2,m2,s2) = timeSearchTwo.split(":")
    timeSearchSplitTwo = datetime.timedelta(hours=int(h2), minutes=int(m2), seconds=int(s2))

    for packageID in range(1,41):
        package = HT.getValue(packageID)
        package.stat(timeSearchSplit,timeSearchSplitTwo)
        print(package)
if int(menu) == 4:
    id = input("Please enter the Id of the package you are looking for")
    timeSearchOne = input("Please enter the start time you wish to see in HH:MM:SS"'\n')
    (h, m, s) = timeSearchOne.split(":")
    timeSearchSplit = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    timeSearchTwo = input("Please enter the end time you wish to see in HH:MM:SS"'\n')
    (h2, m2, s2) = timeSearchTwo.split(":")
    timeSearchSplitTwo = datetime.timedelta(hours=int(h2), minutes=int(m2), seconds=int(s2))
    package = HT.getValue(int(id))
    package.stat(timeSearchSplit, timeSearchSplitTwo)
    print(package)