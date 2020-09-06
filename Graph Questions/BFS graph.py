from collections import defaultdict


class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

        # function to add an edge to graph
    def printg(self):
        return  self.graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, start):
        queue = [start]
        visited = []

        while queue:
            node = queue.pop(0)
            print(node)
            visited.append(node)
            for i in self.graph[node]:
                if i not in visited:
                    queue.append(i)
    def dfs(self, start):
        visited = []
        stack = [start]
        

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print(g.printg())
print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.BFS(2)
g.DFS(2)