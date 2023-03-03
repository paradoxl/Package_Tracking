#Michael Evans
# 010539989
import csv
import datetime
import sys

import packages
from packages import packagesClass
from trucks import trucks
from hashTable import HashTable

HT = HashTable()
#pull in and create trucks
firstTruck = trucks([1,13,14,15,16,19,20,29,30,31,34,37,40],0.0,datetime.timedelta(hours=8),'4001 South 700 East',datetime.timedelta(hours=8))
secondTruck = trucks([3,6,12,17,18,21,22,23,24,26,27,35,36,38,39,25],0.0,datetime.timedelta(hours=9,minutes=5),'4001 South 700 East',datetime.timedelta(hours=9,minutes=5))
# Incorrectly addressed package is on truck 3. It does not leave until after the correct address is discovered.
thirdTruck = trucks([2,4,5,7,8,9,10,11,28,32,33], 0.0,datetime.timedelta(hours=10,minutes=24),'4001 South 700 East',datetime.timedelta(hours=10,minutes=24))


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

        # Create a package object based on data from the CSV
        packageObject = packagesClass(id,address,city,state,zip,deadline,kilo,notes,start,location,status,deliveredAt)
        # Create a instance of the hashTable and assign ID as key and the object as value
        HT.set(id,packageObject)


# calculates distances from row col
# Time complexity O(n^2)
# S(N)
def distanceCalc(r,c):
    with open('data/distanceData.csv',mode='r',encoding='utf-8-sig') as dist:
        distance = 0
        distances = list(csv.reader(dist))
        for i in range(27):
            for j in range(27):
                if distances[i][j] == '' or "":
                    # This line will slowly create a weighted Adjacency Matrix as each location is discovered.
                    distances[i][j] = float(distances[j][i])
                else:
                    distances[i][j] = float(distances[i][j])
                if i == r:
                    if j == c:
                        distance = distances[i][j]
        # This will return the distance from the truck to the next location
        return distance






#return addresses id
#Time Complexity O(n)
# S(N)
def address(val):
    with open("data/locationNames.csv",mode='r',encoding='utf-8-sig') as file:
        names = list(csv.reader(file))
        # Loop through all package names
        for name in names:
            # when address is found that matches package
            if val == name[2]:
                # return the index of the package address. This will correlate with the distances in the matrix above.
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
    # Acts as a staging area to organize packages
    stagingPackages = []
    # Loops throguh each packageID assigned to each truck.
    for packageID in val.packages:
        # Pull package Object from HashTable to variable
        packages = HT.getValue(packageID)
        # Addes package object to staging area
        stagingPackages.append(packages)
        # removes package from truck
    val.packages.clear()
        # organize all packages into truck until staging area empty.
    while len(stagingPackages) > 0:
        # set the next destination to largest num
        newAddress = float(sys.maxsize)
        # set the current package to none
        newPackage = None
        # loop through each package in staging
        for packages in stagingPackages:
            #retruns each truck to the hub
            if len(stagingPackages) == 1:
                # Calculate the distance from the last package to the WGU HUB
                toHub = distanceCalc(int(address(val.address)), int(0))
                # add distance to the truck
                val.time += datetime.timedelta(hours=toHub / 18)
            #checks that the address for package nine is changed. The truck with
            #this package does not leave until after the correct address is identified. So the time factor is not required.
            if packages.id == 9:
                # Assign the correct address to the package.
                packages.address = "410 S State St"
                # Compare the distance from current package to the current lowest distance package
            if distanceCalc((int(address(val.address))), int(address(packages.address))) <= newAddress:
                # If new low is found assign to new low
                newAddress = distanceCalc(address(val.address),address(packages.address))
                # Select the current package
                newPackage = packages
        # Load current lowest value package on truck
        val.packages.append(newPackage)
        # Remove package from staging area
        stagingPackages.remove(newPackage)
        # calculate current distance traveled + the distance to package
        val.distanceTraveled += newAddress
        # assign the truck address to current package address
        val.address = newPackage.address
        # calculate the time it took to reach package address
        val.time += datetime.timedelta(hours=newAddress / 18)
        # Calculate current runtime of package/truck
        newPackage.start = val.statTime
        # calculate the delivery time of the package
        newPackage.deliveredAt = val.time


def hashDemo(value):
    print("Demo:",hash(value))

hashDemo(1)
hashDemo("Test")
hashDemo("test")
hashDemo("Test")

print("-------------------------------------------")
print("Packages assigned to First Truck",firstTruck.packages)
print("Packages assigned to Second Truck:",secondTruck.packages)
print("Packages assigned to Third Truck:",thirdTruck.packages)
#all three trucks are returned to the hub. We could leave two in the world but hey...Realism
#load and deliver packages for first truck
load(firstTruck)
#load and deliver packages for second truck
load(secondTruck)
#load and deliver packages for third truck
load(thirdTruck)
print("-------------------------------------------")
print("Total distance Traveled:", firstTruck.distanceTraveled + secondTruck.distanceTraveled + thirdTruck.distanceTraveled)
print("First truck returned to hub:",firstTruck.time)
print("Second truck returned to hub:",secondTruck.time)
print("Third truck returned to hub:",thirdTruck.time)
print("-------------------------------------------")


menu = input("Welcome! Please select a menu item below."'\n' "1: All packages" '\n'"2: Search specific package packages"'\n' "3: Search all packages based on time"'\n' "4: Search Specific Package based on time"'\n'"-------------------------------------------"'\n')

if int(menu) == 1:
    print("Computing:")
    # Time Complexity O(N)
    for i in range(1,41):
        val = HT.getValue(i)
        val.status = "Delivered"
        print(val)
if int(menu) == 2:
    val = input("Please enter the ID of the package you are looking for"'\n')
    packageVal = HT.getValue(int(val))
    packageVal.status = "Delivered"
    print(packageVal)
if int(menu) == 3:
    timeSearchOne = input("Please enter the start time you wish to see in HH:MM:SS"'\n')
    (h, m, s) = timeSearchOne.split(":")
    timeSearchSplit = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    # Time Complexity O(n)
    for packageID in range(1,41):
        package = HT.getValue(packageID)
        package.stat(timeSearchSplit)
        print(package)
if int(menu) == 4:
    id = input("Please enter the Id of the package you are looking for"'\n')
    timeSearchOne = input("Please enter the start time you wish to see in HH:MM:SS"'\n')
    (h, m, s) = timeSearchOne.split(":")
    timeSearchSplit = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    package = HT.getValue(int(id))
    package.stat(timeSearchSplit)
    print(package)


