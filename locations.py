import csv
import heapq
import sys
from hashTable import HashTable
import packages
table = HashTable()
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
            if(i == src):
                dist[i] = sys.maxsize

        with open("data/locationNames.csv",mode='r', encoding='utf-8-sig') as names:
            name = csv.reader(names)

            for names in name:
                if int(names[0]) == table.getValue(min(dist)):
                    X = 0
            # print("location name for next stop", names[1])
            # print("Location id for next stop", table.getValue(min(dist)))
            # print("minmum distance location from this stop" ,min(dist))
            return table.getValue(min(dist))


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

    # k.shortestPath(3)


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


    # # Tests the shortest path function
    while True:
        counter = 0
        counter2 = 0
        counter3 = 0
        totalDistanceOne = 0
        totalDistanceTwo = 0
        totalDistanceThree = 0
        for row in name:
            for i in range(16):
                #truck one
                if packages.firstTruck()[i][1] == row[2] and packages.firstTruck()[i][8] != 'Delivered':
                    totalDistanceOne += k.shortestPath(int(row[0]))
                    packages.firstTruck()[i][8] = 'Delivered'
                    counter += 1
                    # print(totalDistanceOne)
                    # print("counter for truck one",counter)
                    print("next stop", k.shortestPath(int(row[0])))
                    print("running total", totalDistanceOne)
            for i in range(12):
                #truck two
                if packages.secondTruck()[i][1] == row[2] and packages.secondTruck()[i][8] != 'Delivered':
                    totalDistanceTwo += k.shortestPath(int(row[0]))
                    packages.secondTruck()[i][8] = 'Delivered'
                    counter2 +=1
                    # print("Counter for truck two", counter2)

                #truck thee
                if packages.thirdTruck()[i][1] == row[2] and packages.thirdTruck()[i][8] != 'Delivered':
                    totalDistanceThree += k.shortestPath(int(row[0]))
                    packages.thirdTruck()[i][8] = 'Delivered'
                    counter3 +=1
                    # print("Counter for truck three",counter3)


        total = totalDistanceOne + totalDistanceTwo + totalDistanceThree
        print(total,"Miles driven")
        break
    #

