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
            print(f"{i} \t\t {dist[i]}")
            table.set(dist[i], i)
            if(i == src):
                dist[i] = sys.maxsize
        with open("data/locationNames.csv",mode='r', encoding='utf-8-sig') as names:
            name = csv.reader(names)

            for names in name:
                if int(names[0]) == table.getValue(min(dist)):
                    print("location name for next stop", names[1])
            print("Location id for next stop", table.getValue(min(dist)))
            print("minmum distance location from this stop" ,min(dist))

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
    name = csv.reader(names)
    print(type(packages.firstTruck()))
    for names in name:
        if packages.firstTruck().__contains__(names[1]):

            k.shortestPath(names[0])




