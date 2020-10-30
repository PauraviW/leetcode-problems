from collections import defaultdict, deque


class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
class Clone:
    def cloneg(self, start):
        self.hashTable = defaultdict(Node)
        visited = set()
        queue = deque([start])
        while queue:
            curr = queue.popleft()
            visited.add(curr)
            if curr not in self.hashTable:
                node = Node(curr.val)
                self.hashTable[curr] = node
                for nei in curr.neighbors:
                    if nei in self.hashTable:
                        node.neighbors.append(self.hashTable[nei])

                    else:
                        nnode = Node(nei.val)
                        self.hashTable[nei] = nnode
                        node.neighbors.append(self.hashTable[nei])
                    if nei not in visited:
                        queue.append(nei)







graph = [[1,2],[2,3],[4,5],[5,6],[1,4],[2,4]]
visited = dict()
origin = None
for i, n in graph:
    if i not in visited:


        p = Node(i)
        visited[i] = p
        if not origin:
            origin = p
    if n not in visited:
        c = Node(2)
        visited[n] = c
    p.neighbors.append(c)
    c.neighbors.append(p)

print(Clone().cloneg(p))

