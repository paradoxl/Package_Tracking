import csv
from hashTable import HashTable

truckOne = [] #leaves asap
truckTwo = [] #levas at 1030
truckThree = [] #contains remaining packages. Truck one will drive this after completion.
class package:
    def __int__(self):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.kilo = kilo
        self.notes = notes
        self.start = start
        self.location = location
        self.status = status


with open("data/packageData.csv") as file:
    reader = csv.reader(file)
    #pull data in to variables
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
        #assemble variables into package object
        package = [id,address,city,state,zip,deadline,kilo,notes,start,location,status]
        #assign packages to truck two
        if 'Can' in package[7]:
            truckTwo.append(package)
        if 'Delayed' in package[7] and '10:30' not in package[7]:
            truckTwo.append(package)
        if 'Wrong' in package[7]:
            truckTwo.append(package)
        #Assign packages to truck one
        if 'EOD' not in package[5]:
            truckOne.append(package)
        if package[0] == '2' or package[0] == '4':
            truckOne.append(package)


        if package not in truckOne and package not in truckTwo and package not in truckThree:
            if len(truckTwo) < len(truckThree):
                truckTwo.append(package)

            else:
                truckThree.append(package)
        if package[0] == '6' or package[0] == '25':
            truckTwo.remove(package)
            #13,14,15,16,19,20
print('truck one:',len(truckOne))
print('truck two',len(truckTwo))
print('truck three', len(truckThree))

i = 0

for packages in truckOne:
    print(truckOne[i])
    i = i + 1
i = 0
print(" ")
for packages in truckTwo:
    print(truckTwo[i])
    i = i + 1
i = 0
print(" ")
for packages in truckThree:
    print(truckThree[i])
    i = i + 1