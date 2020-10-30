import heapq


class Solution:
    def minMeetingRooms(self, intervals: [[int]]) -> int:
        heap = []
        intervals.sort(key = lambda x: x[0])
        count = 0
        for s, t in intervals:
            if not heap:
                heapq.heappush(heap, t)
                count += 1
            else:
                curr = heapq.heappop(heap)
                if curr > s:
                    heapq.heappush(heap, t)
                    count += 1
                else:
                    heapq.heappush(heap, curr)
        return count
print(Solution().minMeetingRooms([[7,10],[2,4]]))