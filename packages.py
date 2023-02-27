import csv
from hashTable import HashTable
truckOne = [] #leaves asap
truckTwo = [] #levas at 1030
truckThree = [] #contains remaining packages. Truck one will drive this after completion.
class packagesClass:
    def __init__(self,id,address,city,state,zip,deadline,kilo,notes,start,location,status,deliveredAt):
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
        self.deliveredAt = deliveredAt



    def __str__(self):
        return "%s,%s,%s%s,%s,%s"%("ID:",self.id,"Delivery Status: ",self.status,"Delivered At: ",self.deliveredAt)