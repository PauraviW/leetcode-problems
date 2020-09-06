from collections import defaultdict


# This class represents a directed graph using adjacency list
# representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary
        # Add w to the list of v
    def addEdge(self, v, w):
        self.graph[v].append(w)
    def countPaths(self, start, end):
        total = [0]
        visited = self.V * [False]
        self.DFS(start, end, total, visited)
        return  total[0]
    def DFS(self, root, end,  total, visited):
        visited[root] = True
        if root  == end:
            total[0] += 1
        else:
            for i in self.graph[root]:
                if not visited[i]:
                    self.DFS(i, end, total, visited)
        visited[root] = False





g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)

s = 2
d = 3
print(g.countPaths(s, d))
