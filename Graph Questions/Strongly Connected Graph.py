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
    def dfs(self, graph):
        visited = defaultdict(bool)
        for k, v in graph.items():
            visited[k] = False
            for j in v:
                visited[j] = False
        vertex = list(graph.keys())[0]
        queue = [vertex]
        while queue:
            node = queue.pop()
            visited[node] = True
            temp = []
            for i in graph[node]:
                if not visited[i]:
                    temp.append(i)
            queue += temp[::-1]
        return [k for k, v in visited.items() if not v]


    def checkStrongConnection(self):
        if self.graph:
            # dfs
            val = self.dfs(self.graph)
            # print(val)
            if len(val) > 0:
                 return False
            #
            reverseDict = defaultdict(list)
            for k, v in self.graph.items():
                 for j in v:
                     reverseDict[j].append(k)
            val = self.dfs(reverseDict)
            print(val)
            if len(val) > 0:
                return False
            return True







g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)
g1 = Graph()
g1.addEdge(0, 1)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.addEdge(3, 0)
g1.addEdge(2, 4)
g1.addEdge(4, 2)
g2 = Graph()
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print(g1.printg())
print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
print(g1.checkStrongConnection())
print(g2.checkStrongConnection())