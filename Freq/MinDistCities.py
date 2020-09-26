numOfCities = 3
cities = ["c1", "c2", "c3"]
xCoordinates = [3,2,1]
yCoordinates = [3,2,3]
numOfQueries = 3
queries = ["c1", "c2", "c3"]
def getDistance(x1, y1, x2, y2):
    distance = abs(x1 - x2) + abs(y1 - y2)


    return distance


result = []


d = {}
for i, city in enumerate(cities):
    d[city] = i


def getNeighbours(queryCity):
    finalindex = -1
    minDist = float("inf")
    ind = d[queryCity]
    x = xCoordinates[ind]
    y = yCoordinates[ind]

    for i in range(0, numOfCities):
        if i != ind and (xCoordinates[i] == x or yCoordinates[i] == y):
            distance = getDistance(x, y, xCoordinates[i], yCoordinates[i])
            if distance < minDist:
                minDist = distance
                finalindex = i
            elif distance == minDist:
                if cities[i] < cities[finalindex]:
                    finalindex = i
    return finalindex


for city in queries:
    temp = getNeighbours(city)
    if temp == -1:
        result.append(None)
    else:
        result.append(cities[temp])

print(result)


