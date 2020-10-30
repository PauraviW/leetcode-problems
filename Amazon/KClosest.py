import heapq
import math


class Closest:
    def KClosest(self, points, k):

        ans = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            if len(ans) >= k:
                heapq.heappop(ans)
            heapq.heappush(ans ,(-dist, (x,y)))
        return [x[1] for x in ans]

points = [[1,4], [56,2], [12,34], [45,67], [12,45]]
print(Closest().KClosest(points, 4))