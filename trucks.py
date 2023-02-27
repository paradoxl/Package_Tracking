import datetime


class trucks:
    def __init__(self,packages,distanceTraveled,time,address,statTime):
        self.packages = packages
        self.distanceTraveled = distanceTraveled
        self.time = time
        self.statTime = statTime
        self.address = address

    def printTruck(self):
        print(self.packages,self.distanceTraveled,self.time,self.address)

