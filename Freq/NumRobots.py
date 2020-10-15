def dist(p1, p2):
    return (p1[0] - p2[0])**2  + (p1[1] - p2[1])**2
def stripClosest(strip, size, d):
    mind = d
    strip.sort(key = lambda x: x[1])
    for i in range(size):
        j = i + 1
        while  j < size and (strip[j][1] - strip[i][1]) < mind:
            mind = dist(strip[i], strip[j])
            j += 1
    return mind
def bruteForce(points):
    mind =  float("inf")
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if dist(points[i], points[j]) < mind:
                mind = dist(points[i], points[j])
    return mind
def closestUtil(points, n):

    if n <= 3:
        return bruteForce(points)

    # middle
    mid = n // 2
    midpoint = points[mid]

    dl = closestUtil(points[:mid], mid)
    dr = closestUtil(points[mid:], n-mid)

    d = min(dl, dr)
    strip = []
    for i in range(n):
        if abs(points[i][0] - midpoint[0]) < d:
            strip.append(points[i])
    return min(d, stripClosest(strip, len(strip), d))


def closest(points, n):
    points.sort(key = lambda x:x[0])
    print(points)
    return closestUtil(points, n)

positionX = [0,1,2]
positionY = [0,1,4]
positionX = [12,40, 5, 12, 3]
positionY = [30,50, 1,10, 4]
points = set()
for i in range(len(positionX)):
    points.add((positionX[i], positionY[i]))

points = list(points)
print(closest(points, len(points)))
