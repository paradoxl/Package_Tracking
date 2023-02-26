import csv
import datetime
import sys

from trucks import trucks
from hashTable import HashTable

#pull in and create trucks
#Time complexity O(1)
firstTruck = trucks([1,13,14,15,16,20,29,30,31,34,37,40],0.0,datetime.timedelta(hours=8),'4001 South 700 East')
secondTruck = trucks([3,6,12,17,18,19,21,22,23,24,26,27,35,36,38,39],0.0,datetime.timedelta(hours=10,minutes=30),'4001 South 700 East')
thirdTruck = trucks([2,4,5,6,7,8,9,10,11,25,28,32,33], 0.0,datetime.timedelta(hours=9,minutes=5),'4001 South 700 East')

#generate packages
#Time complexity O(n)
with open("data/packageData.csv",mode='r',encoding='utf-8-sig') as file:
    HT = HashTable()
    PL = HashTable()
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
        HT.set(int(id),package[1])
        PL.set(int(id),package)

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
def packageList():
    with open('data/packageData.csv',mode='r',encoding='utf-8-sig') as pData:
        reader = csv.reader(pData)
        for row in reader:
            value = PL.getValue(int(row[0]))
            print(value)
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

    not_delivered = []
    for packageID in val.packages:
        packages = HT.getValue(packageID)
        not_delivered.append(packages)
    val.packages.clear()
    while len(not_delivered) > 0:
        newAddress = float(sys.maxsize)
        newPackage = None
        for packages in not_delivered:
            if distanceCalc(int(address(val.address)), int(address(packages))) <= newAddress:
                newAddress = distanceCalc(address(val.address),address(packages))
                newPackage = packages
        val.packages.append(newPackage)
        not_delivered.remove(newPackage)
        val.distanceTraveled += newAddress
        val.address = newPackage
        val.time += datetime.timedelta(hours=newAddress / 18)
        newPackage = val.time
        newPackage = val.time
def runRoute():
    load(firstTruck)
    thirdTruck.time = firstTruck.time
    load(secondTruck)
    load(thirdTruck)
    print("Total distance Traveled", firstTruck.distanceTraveled + secondTruck.distanceTraveled + thirdTruck.distanceTraveled)
    print("First truck returned to hub",firstTruck.time)
    print("Second truck returned to hub",secondTruck.time)
    print("Third truck returned to hub",thirdTruck.time)
runRoute()

