import csv
import heapq

# iPair ==> Integer Pair
iPair = tuple


# This class represents a directed graph using
# adjacency list representation
class Graph:
    def __init__(self, V: int):  # Constructor
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdge(self, u: int, v: int, w: float):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    # Prints shortest paths from src to all other vertices
    def shortestPath(self, src: int):
        # Create a priority queue to store vertices that
        # are being preprocessed
        pq = []
        heapq.heappush(pq, (0, src))

        # Create a vector for distances and initialize all
        # distances as infinite (INF)
        dist = [float('inf')] * self.V
        dist[src] = 0

        while pq:
            # The first vertex in pair is the minimum distance
            # vertex, extract it from priority queue.
            # vertex label is stored in second of pair
            d, u = heapq.heappop(pq)

            # 'i' is used to get all adjacent vertices of a
            # vertex
            for v, weight in self.adj[u]:
                # If there is shorted path to v through u.
                if dist[v] > dist[u] + weight:
                    # Updating distance of v
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))

        # Print shortest distances stored in dist[]
        for i in range(self.V):
            print(f"{i} \t\t {dist[i]}")


# Driver's code
if __name__ == "__main__":
    # create the graph given in above figure

    v = 27
    k = Graph(v)

    for i in range(27):
        for j in range(27):


    k.addEdge(0,1,7.2)
    k.addEdge(0,2,3.8)
    k.addEdge(0,3,11)
    k.addEdge(0,4,2.2)
    k.addEdge(0,5,3.5)
    k.addEdge(0,6,10.9)
    k.addEdge(0,7,8.6)
    k.addEdge(0,8,7.6)
    k.addEdge(0,9,5.2)
    k.addEdge(0,10,4.4)
    k.addEdge(0,11,3.7)
    k.addEdge(0,12,7.6)
    k.addEdge(0,13,2.0)


    k.shortestPath(0)

with open("data/distanceData.csv",mode='r',encoding='utf-8-sig') as distance:
    distances = list(csv.reader(distance))


