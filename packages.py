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

    def stat(self, time1, time2):
        # if self.deliveredAt > time1:
        #     self.status = "in route"
        #     self.deliveredAt = "Not yet delivered"
        # elif self.start < time1:
        #      self.status = "test"
        # else:
        #     self.status = "At Hub"
        #     self.deliveredAt = "Not yet delivered"
        if self.deliveredAt > time1 and self.start < time1:
            self.status = "in route"
            self.deliveredAt = "On the way"
        elif self.start < time1:
            self.status = "Delivered"
        else:
            self.status = "At hub"
            self.deliveredAt = "Package not yet out for delivery"

    def __str__(self):
        return "%s%s%s%s%s%s"%("ID:",self.id," Delivery Status: ",self.status," Delivered At: ",self.deliveredAt)

