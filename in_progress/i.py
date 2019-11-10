# Kari Hoff

from heapq import heappush, heappop

class Vertex:
    def __init__(self, key):
        self.ID = key
        self.connectedTo = {}
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    def __str__(self):
        return str(str(self.ID) + ' connected to ' + str([x.ID for x in self.connectedTo]))
    def getConnections(self):
        return self.connectedTo.keys()
    def getID(self):
        return self.ID
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVerts = 0
    def __contains__(self, n):
        return n in self.vertList
    def addVertex(self, key):
        self.numVerts += 1
        newVert = Vertex(key)
        self.vertList[key] = newVert
        return newVert
    def addEdge(self, fromVert, toVert, weight=0):
        if fromVert not in self.vertList:
            nv = self.addVertex(fromVert)
        if toVert not in self.vertList:
            nv = self.addVertex(toVert)
        self.vertList[fromVert].addNeighbor(self.vertList[toVert], weight)
        self.vertList[toVert].addNeighbor(self.vertList[fromVert], weight)

    def getVertex(self, vertKey):
        if vertKey in self.vertList:
            return self.vertList[vertKey]
        else:
            return None
    def getVertices(self):
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())

def Dijkstra(graph, start):
    A = [None] * graph.numVerts
    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        print(f"V:{v}")
        if A[v-1] is None:
            A[v-1] = path_len
            vertex = graph.getVertex(v)
            for neighborVertex in vertex.getConnections(): # issue here
                # w
                # edge_len
                if A[neighborVertex.getID()] is None:
                    w = neighborVertex.getWeight(vertex)
                    heappush(queue, (path_len + w, w))
                if A[w] is None:
                    heappush(queue, (path_len + vertex.getWeight(neighborVertex), w))
    return [0 if x is None else x for x in A]

taxDict = {}
shortestPaths = {}
graph = Graph()

# Add Cities to Graph
n = int(input())
for i in range(n):
    graph.addVertex(i+1)

# Add Taxes to taxDict
taxes = input().strip().split()
for i in range(len(taxes)):
    taxDict[i+1] = int(taxes[i])

# Add Edges to Graph
for i in range(n-1):
    line = input()
    u, v, w = line.strip().split()
    u, v, w = int(u), int(v), int(w)
    graph.addEdge(u, v, w)

# Call Dijkstra for each city
for i in range(n):
    print(Dijkstra(graph, i+1))