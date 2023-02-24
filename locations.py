import csv
import functools
import heapq
import sys
from hashTable import HashTable
import packages
from datetime import time, timedelta

table = HashTable()
reverse = HashTable()
class Graph:
    def __init__(self, V: int):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdge(self, u: int, v: int, w: float):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def shortestPath(self, src: int):

        pq = []
        heapq.heappush(pq, (0, src))
        dist = [float('inf')] * self.V
        dist[src] = 0

        while pq:
            d, u = heapq.heappop(pq)

            for v, weight in self.adj[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))

        #retruns the min value and sets current location to max value to not create loop
        for i in range(self.V-1):
            # print(f"{i} \t\t {dist[i]}")
            table.set(dist[i], i)
            reverse.set(i,dist[i])
            if(i == src):
                dist[i] = sys.maxsize

        with open("data/locationNames.csv",mode='r', encoding='utf-8-sig') as names:
            name = csv.reader(names)

            for names in name:
                if int(names[0]) == table.getValue(min(dist)):
                    X = min(dist)
            # print("location name for next stop", names[1])
            # print("Location id for next stop", table.getValue(min(dist)))
            # print("minmum distance location from this stop" ,min(dist))
            #

            return reverse.getValue(table.getValue(min(dist)))


    # create the graph given in above figure
with open("data/distanceData.csv" ,encoding='utf-8-sig') as distance:
    distances = list(csv.reader(distance))
    v = 27
    k = Graph(v)
    for i in range(27):
        for j in range(27):
            if distances[i][j] == "" or '':
                k.addEdge(i,j,sys.maxsize)
            else:
                weight = float(distances[i][j])
                k.addEdge(i,j,weight)


with open( "data/locationNames.csv", mode='r', encoding='utf-8-sig') as names:
    name = list(csv.reader(names))
#
#     def locationNames():
#         return name
#
# with open("data/distanceData.csv", mode='r',encoding='utf-8-sig') as distances:
#     dist = list(csv.reader(distances))
#     def distance(r,c):
#         distances = dist[r][c]
#         if distances  == '' or "":
#             distances = dist[c][r]
#         t =+ float(distances)
#         return t
#
#     # pulls in travel time and formats to hour and minute
#     # time complexity: O(n)
#     def truckDistance(dist, schedule):
#         timeDist = dist/18
#         timeMin = '{0:02.0f}:{1:02.0f}'.format(*divmod(timeDist * 60,60))
#         return timeMin
#
#     print(truckDistance(100,1))
#     print(len(packages.firstTruck()))
#     print(packages.firstTruck())
#     print(locationNames())

    # print(packages.secondTruck())
    # print(packages.thirdTruck())
# Tests the shortest path function
    def hub(location):
        helper = 69
        helper = distances[location][0]
        return float(helper)


    def distToTime(distance):
        t = distance / 18
        _time = (distance * 3600) / 18
        mins = '{0:02.0f}:{1:02.0f}'.format(*divmod(t * 60, 60))
        test = divmod(t*60,60)
        res = functools.reduce(lambda sub, ele: sub * 10 + ele, test)
        conv = '{0:02.0f}:{1:02.0f}'.format(*divmod(res * 60, 60))
        print("conversion",conv)
        print(type(conv))
        return mins


    for i in range(16):
        packages.firstTruck()[i][10] = 'In Transit'
    for i in range(12):
        packages.secondTruck()[i][10] = 'In Transit'
    # print("Packages",packages.firstTruck()[1][1])
    first = True
    first2 = True
    first3 = True


    truckOneLeaveTime = time(10,30,00)
    dTime = 0.0

    #Time complexity O(n^3)
    while True:
        counter = 0
        counter2 = 0
        counter3 = 0
        total = 0
        totalDistanceTwo = 0
        totalDistanceThree = 0
        secondDriverDone = False


        for row in name:
            for i in range(16):
                #truck one
                if packages.firstTruck()[i][1] == row[2] and packages.firstTruck()[i][10] != 'Delivered':
                    packageLocation = packages.firstTruck()[i][1]
                    if first is True:
                        total += hub(int(row[0]))
                        first = False

                    total += k.shortestPath(int(row[0]))
                    truckOneLeaveTime = distToTime(int(row[0]))
                    print(int(row[0]))
                    packages.firstTruck()[i][10] = 'Delivered'
                    packages.firstTruck()[i][11] = 'Delivered at: ', truckOneLeaveTime

            for i in range(12):
                #truck two
                if packages.secondTruck()[i][1] == row[2] and packages.secondTruck()[i][10] != 'Delivered':
                    if first2 is True:
                        total += hub(int(row[0]))
                        first2 = False
                    total += k.shortestPath(int(row[0]))
                    packages.secondTruck()[i][10] = 'Delivered'
                    if int(i) == int(11):
                        #from current to hub
                        total += hub(int(row[0]))
                        secondDriverDone = True

            for i in range(12): #truck thee
                    if packages.thirdTruck()[i][1] == row[2] and packages.thirdTruck()[i][10] != 'Delivered':
                        if first3 is True:
                            total += hub(int(row[0]))
                            first3 = False

                        total += k.shortestPath(int(row[0]))
                        packages.thirdTruck()[i][10] = 'Delivered'

        # print(packages.secondTruck())

        print(total,"Miles driven")
        packages.packageList()

        break
    #

