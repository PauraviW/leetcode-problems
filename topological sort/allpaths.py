from collections import defaultdict
edges = [[5,2], [5,0],[4,0],[4,1],[2,3],[3,1]]
neighbors = defaultdict(list)
indegree = defaultdict(int)
vertices = set()
for e1, e2 in edges:
    neighbors[e1].append(e2)
    indegree[e2] += 1
    vertices.add(e1)
    vertices.add(e2)
v = len(vertices)
visited = [False for i in range(v)]

def topologicalutil(visited, indegree, stack=[]):

    flag = False

    for i in range(v):
        if not visited[i] and indegree[i] == 0:
            visited[i] = True
            stack.append(i)
            for nei in neighbors[i]:
                indegree[nei] -= 1
            topologicalutil(visited, indegree, stack)

            visited[i] = False
            stack.pop()
            for nei in neighbors[i]:
                indegree[nei] += 1
            flag = True

    if not flag:
        print(stack)


topologicalutil(visited, indegree, [])