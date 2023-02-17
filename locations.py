import csv


class graph(object):
    def __init__(self,size):
        self.matrix = []
        for i in range(size):
            self.matrix.append([0 for i in range(size)])
            self.size = size
    def addEdges(self,vertexOne,vertexTwo):
            if vertexOne == vertexTwo:
                print("This is the same location")
            self.matrix[vertexOne][vertexTwo] = 1
            self.matrix[vertexTwo][vertexOne] = 1
    def removeEdge(self,vertexOne,vertexTwo):
           if self.matrix[vertexOne][vertexTwo] == 0:
               print("No route available")
               return
           self.matrix[vertexOne][vertexTwo] = 0
           self.matrix[vertexTwo][vertexOne] = 0

    def __len__(self):
        return self.size

    def showRoutes(self):
        for row in self.matrix:
            for values in row:
                print(values)



with open("data/locationNames.csv") as locationNames:
    reader = csv.reader(locationNames)

    for rows in reader:
        id = rows[0]
        name = rows[1]
        address = rows[2]

        
