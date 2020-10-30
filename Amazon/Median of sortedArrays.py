import heapq


class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        low = 0
        high = m 
        while low <= high:
            partitionX = int((low + high) / 2)
            partitionY = int((m + n + 1) / 2) - partitionX

            maxLeftX = nums1[partitionX - 1] if partitionX > 0 else -float('inf')
            minRightX = nums1[partitionX] if partitionX < m else float('inf')
            maxLeftY = nums2[partitionY - 1] if partitionY > 0 else -float('inf')
            minRightY = nums2[partitionY] if partitionY < n else float('inf')

            if maxLeftX <= minRightY and maxLeftY <= minRightX:

                if (m + n) % 2 == 0:
                    return sum(max(maxLeftX, maxLeftY) + min(minRightY, minRightX)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            else:
                if maxLeftX > minRightY:
                    high = partitionX - 1
                else:
                    low = partitionX + 1


#         m = len(nums1)
#         n = len(nums2)
#         low = 0
#         high = m
#         while low <= high:
#             partitionx = int((low + high)/2)
#             partitiony = int ((m+n+1)/2) - partitionx
#             if partitionx > 0:
#                 maxLeftX = nums1[partitionx - 1]
#             else:
#                 maxLeftX = -float('inf')
#             if partitionx < m-1:
#                 minRightX = nums1[partitionx + 1]
#             else:
#                 minRightX = float('inf')
#             maxLeftY = nums2[partitiony - 1] if partitiony > 0 else -float('inf')
#             minRightY = nums2[partitionx - 1] if partitiony < n-1 else float('inf')
#
#             if maxLeftX <= minRightY and maxLeftY <= minRightX:
#                 if (m+n) % 2 == 0:
#                     return sum(max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
#                 else:
#                     return max(maxLeftX, maxLeftY)
#             else:
#                 if maxLeftX > minRightY:
#                     high = partitionx - 1
#                 else:
#                     low  = partitionx + 1
print(Solution().findMedianSortedArrays([1,3],[2]))


#         minHeap = []
#         maxHeap = []
#
#         for num in nums1:
#
#             heapq.heappush(maxHeap, -num)
#             val = heapq.heappop(maxHeap)
#             heapq.heappush(minHeap, -val)
#             if len(minHeap) > len(maxHeap):
#                 val = heapq.heappop(minHeap)
#                 heapq.heappush(maxHeap, -val)
#         for num in nums2:
#
#             heapq.heappush(maxHeap, -num)
#             val = heapq.heappop(maxHeap)
#             heapq.heappush(minHeap, -val)
#             while len(minHeap) > len(maxHeap):
#                 val = heapq.heappop(minHeap)
#                 heapq.heappush(maxHeap, -val)
#         if len(maxHeap) > len(minHeap):
#             return - heapq.heappop(maxHeap)
#         else:
#             return ((-heapq.heappop(maxHeap)) + heapq.heappop(minHeap)) / 2
#
# print(Solution().findMedianSortedArrays([1,3],[2]))
#
