#Michael Evans 010539989
import csv
from pandas import *

# Class to hold data on packages
class packages:
    def __init__(self, id, address, city, state, zip, deliveryDeadline, massKilo, specialNotes ):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryDeadline = deliveryDeadline
        self.massKilo = massKilo
        self.specialNotes = specialNotes

# Class to hold data on locations
class location:
    def __init__(self,  name, address,  distance):

        self.name = name
        self.address = address

        self.distance = distance
# Class to hold hashtable/spicy dictionary
class HashTable:
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
    def insert(self, key, item):
        #
        bucket = hash(key) % len(self.table)
        hashList = self.table[bucket]

        for keyPair in hashList:
            # print (key_value)
            if keyPair[0] == key:
                keyPair[1] = item
                return True
        key_value = [key, item]
        hashList.append(key_value)
        return True

    def search(self, key):
        bucket = hash(key) % len(self.table)
        hashList = self.table[bucket]

        for keyPair in hashList:
            if keyPair[0] == key:
                return keyPair[1]
        return None

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        hashList = self.table[bucket]

        for keyPair in hashList:
            if keyPair[0] == key:
                hashList.remove([keyPair[0], keyPair[1]])

#pull data in on packages
with open('data/packageData.csv', mode='r') as f:
        reader = csv.reader(f)
        packageList = []
        for row in reader:
            id = row[0]
            address = row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            deadline = row[5]
            mass = row[6]
            notes = row[7]
            test = 9
            package = packages(id, address,city,state,zip,deadline,mass,notes)
            packageList.append(package)
#pull location data
with open('data/distanceTest.csv', mode='r') as f:
        reader = csv.reader(f)
        locationList = []
        for row in reader:
            name = row[0]
            address = row[1]
            distance = row[2]
            locationObject = location(name, address,distance)
            locationList.append(locationObject)


for packages in packageList:
    i = 0
    if packageList[i].address == locationList[4].address:
        print("Match")
    i = i + 1

