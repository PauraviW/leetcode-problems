import heapq
from collections import Counter


def removeIds(ids, m):

    countDict = Counter(ids)

    heap = []
    for k, v in countDict.items():
        heapq.heappush(heap, (v, k))

    while heap and m:
        val, id = heapq.heappop(heap)
        if val <= m:
            m -= val
        else:
            m = 0
            heapq.heappush(heap, (val-m, id))

    return len([i[1] for i in heap])

ids = [ 2, 4, 1, 5, 3, 5, 1, 3]
m = 2
print(removeIds(ids, m))
