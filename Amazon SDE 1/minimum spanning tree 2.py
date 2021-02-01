import heapq
from collections import defaultdict

n = 5
edges = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
edgesToRepair = [[1, 2, 12], [3, 4, 30], [1, 5, 8]]
visited =set()
mincost = float('inf')



def minCostToRepairEdges(n, edges, edgesToRepair):

    graph = defaultdict(list)
    addedEdges = set()
    for edge in edgesToRepair:
        graph[edge[0]].append((edge[2], edge[1]))
        graph[edge[1]].append((edge[2], edge[0]))
        addedEdges.add((edge[0], edge[1]))
        addedEdges.add((edge[1], edge[0]))
    for edge in edges:
        if tuple(edge) not in addedEdges:
            graph[edge[0]].append((0, edge[1]))
            graph[edge[1]].append((0, edge[0]))

    res = 0
    priorityQueue = [(0, 1)]
    heapq.heapify(priorityQueue)
    visited = set()

    while priorityQueue:
        minCost, node = heapq.heappop(priorityQueue)
        if node not in visited:
            visited.add(node)
            res += minCost
            for cost, connectedNode in graph[node]:
                if connectedNode not in visited:
                    heapq.heappush(priorityQueue, (cost, connectedNode))
    return res if len(visited) == n else  -1

edgesToRepair = [[1, 4, 100], [2, 4, 10], [2, 3, 7], [2, 5, 15], [2, 1, 17], [5, 3, 1]]

n = 1
edges = []
edgesToRepair = []
print(minCostToRepairEdges(n, edges, edgesToRepair))

