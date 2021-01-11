from collections import defaultdict, deque
#
n = 4
m = 3
max_t = 49
beauty = [0,32, 10, 43]
u = [0,2,0]
v = [1,0,3]
t = [10, 13, 17]

####################
# n = 5
# m = 6
# max_t = 70
# beauty = [30,80, 100, 50, 50]
# u = [4,1,0,4,2,2]
# v = [3,4,3,0,3,0]
# t = [20, 15, 40, 10, 100, 10]
class ts:
    def __init__(self):
        self.max_beaut = 0
    def dfs(self, curr, visited, cb, cc):

        if cc > max_t:
            return
        if curr == 0:
            self.max_beaut = max(self.max_beaut, cb)
        for neighbor in neighbors[curr]:
            # if neighbor not in visited:

            if neighbor in visited:
                self.dfs(neighbor, visited, cb, cc + adj[curr, neighbor])
            else:
                visited.add(neighbor)
                self.dfs(neighbor, visited, cb+beauty[neighbor], cc + adj[curr, neighbor])
                visited.remove(neighbor)





attractions = set([0])
visited = set()
adj = defaultdict(int)
neighbors = defaultdict(list)
for i in range(len(u)):
    adj[(u[i],v[i])] = t[i]
    adj[(v[i],u[i])] = t[i]
    neighbors[u[i]].append(v[i])
    neighbors[v[i]].append(u[i])

v = ts()
v.dfs(0, {0}, beauty[0],0)
print(v.max_beaut)




