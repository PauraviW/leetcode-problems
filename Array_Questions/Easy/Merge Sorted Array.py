class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        i = 0
        while len(nums1) != m:
            nums1.pop()
        while nums2:
            val = nums2.pop(0)
            while i < len(nums1) and nums1[i] <= val:
                i += 1
            nums1.insert(i, val)
        print(nums1)







nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3
print(Solution().merge(nums1, m, nums2, n))