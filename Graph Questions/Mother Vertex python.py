from collections import defaultdict


# This class represents a directed graph using adjacency list
# representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary
        # Add w to the list of v
    def DFS(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.DFS(i, visited)

    def addEdge(self, v, w):
        self.graph[v].append(w)
    def find_mother(self):
        visited = [False] * self.V
        v = 0
        for i in range(self.V):
            if visited[i] == False:
                self.DFS(i, visited)
                v = i

        visited = [False] * (self.V)
        self.DFS(v, visited)
        if any(i == False for i in visited):
            return -1
        else:
            return v



g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(4, 1)
g.addEdge(6, 4)
g.addEdge(5, 6)
g.addEdge(5, 2)
g.addEdge(6, 0)
print(g.find_mother())