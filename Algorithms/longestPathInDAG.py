import sys
class LongestPathClass:

    def __init__(self, contents):
        self.graphData = contents
        self.adj = {}
        self.edgeWeight = {}
        self.startNode = int(self.graphData[0])
        self.endNode = int(self.graphData[1])

    def nodeList(self):

        for edge in self.graphData[2:]:
            nodeData = list(edge.split('->'))
            if int(nodeData[0]) not in self.adj:
                self.adj[int(nodeData[0])] = 0
            else:
                continue
        return

    def getEdges(self):
        for i in range(len(self.adj)):
            endNodes = []
            for edge in self.graphData[2:]:
                vertexData = list(edge.split('->'))
                edgeData = list(vertexData[1].split(':'))
                if int(vertexData[0]) == i:
                    endNodes.append(int(edgeData[0]))
            self.adj[i] = endNodes
        self.adj[self.endNode] = []
        return

    def weightData(self):
        for edge in self.graphData[2:]:
            split = edge.split(":")
            self.edgeWeight[split[0]] = int(split[1])
        return

    def longestPath(self, v, visited=None, path=None):
        if visited is None:
            visited = [v]
        if path is None:
            path = [v]
        paths = []
        for t in self.adj[v]:
            if t not in visited and t in self.adj:
                t_path = path + [t]
                paths.append(t_path)
            else:
                break
            paths.extend(self.longestPath(t, visited[:], t_path))
        return paths

    def calculateWeight(self, pathString):
        maxWeight = 0
        bestPath = ''
        for path in pathString:
            totalWeight = 0
            for weight in self.edgeWeight:
                if weight in path:
                    totalWeight += self.edgeWeight[weight]
            if totalWeight > maxWeight:
                maxWeight = totalWeight
                bestPath = path
            else:
                continue
        return maxWeight, bestPath

if __name__ == "__main__":
    graphData = []
    data = None
    with open('rosalind_ba5d.txt', 'r') as f:
        data = f.readlines()
        print(data)
        for d in data:
            graphData.append(d.strip('\n'))

    graph = LongestPathClass(graphData)
    graph.nodeList()
    graph.getEdges()
    graph.weightData()
    paths = graph.longestPath(int(graphData[0]))
    completePaths = []
    for path in paths:
        if path[0] == int(graphData[0]) and path[-1] == int(graphData[1]):
            completePaths.append(path)
    pathStringName = []
    for path in completePaths:
        pathString = graphData[0]
        for node in path[1:]:
            pathString += '->' + str(node)
        pathStringName.append(pathString)
    maxWeight, longestPath = graph.calculateWeight(pathStringName)
    print(f'{maxWeight}\n{longestPath}')


