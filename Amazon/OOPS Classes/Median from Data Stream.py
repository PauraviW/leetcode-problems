# Median is the middle value in an ordered integer list. If the size of the list is even
# , there is no middle value. So the median is the mean of the two middle value.
#
# For example,
# [2,3,4], the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Design a data structure that supports the following two operations:
#
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
import heapq


class Median:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
    def add(self, num):

        heapq.heappush(self.maxHeap, -num)
        val = heapq.heappop(self.maxHeap)
        heapq.heappush(self.minHeap, -val)
        if len(self.minHeap) > len(self.maxHeap):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)


    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0])/2
        else:
            return -self.maxHeap[0]