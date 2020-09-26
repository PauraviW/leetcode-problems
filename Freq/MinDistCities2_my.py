from collections import defaultdict

numOfCities = 3
cities = ["c1", "c2", "c3"]
xCoordinates = [3,2,1]
yCoordinates = [3,2,3]
numOfQueries = 3
queries = ["c1", "c2", "c3"]
distMap = defaultdict(list)
distMap_x = defaultdict(list)
distMap_y = defaultdict(list)
for i in range(len(cities)):
    distMap[cities[i]] += [xCoordinates[i], yCoordinates[i]]
    distMap_x[xCoordinates[i]].append(cities[i])
    distMap_y[yCoordinates[i]].append(cities[i])
ans = []
for i in queries:
    q_x, q_y = distMap[i]
    dist_map = defaultdict(list)
    for p in distMap_x[q_x]:
        if p != i:
            dist = abs(distMap[p][0] - q_x) + abs(distMap[p][1] - q_y)
            dist_map[dist].append(p)
    for p in distMap_y[q_y]:
        if p != i:
            dist = abs(distMap[p][0] - q_x) + abs(distMap[p][1] - q_y)
            dist_map[dist].append(p)
    if len(dist_map) > 0:
        min_d = min(dist_map.keys())
        ans.append(min(dist_map[min_d]))
    else:
        ans.append(None)
print(ans)


