import datetime


class trucks:
    def __init__(self,packages,distanceTraveled,time,address):
        self.packages = packages
        self.distanceTraveled = distanceTraveled

        self.time = time
        self.address = address

    def printTruck(self):
        print(self.packages,self.distanceTraveled,self.time,self.address)

    def printTruckOne(self):
        return