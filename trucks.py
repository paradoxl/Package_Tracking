import datetime


class trucks:
    def __init__(self,packages,distanceTraveled,currLoc,time):
        self.packages = packages
        self.distanceTraveled = distanceTraveled
        self.currLoc = currLoc
        self.time = time

    def printTruck(self):
        print(self.packages,self.distanceTraveled,self.currLoc,self.time)

    def printTruckOne(self):
        return