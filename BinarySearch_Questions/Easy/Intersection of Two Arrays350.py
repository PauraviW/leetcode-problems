class Solution:
    def intersect(self, nums1: [], nums2: []) -> []:
        nums1.sort()
        nums2.sort()
        if nums1 == nums2:
            return nums1
        d = {}
        ans = []
        if len(nums1) > len(nums2):
            for i in nums1:
                d[i] = d.get(i, 0) + 1
            for i in nums2:
                if d.get(i, 0) > 0:
                    ans.append(i)
                    d[i] -= 1
        else:
            for i in nums2:
                d[i] = d.get(i, 0) + 1
            for i in nums1:
                if d.get(i, 0) > 0:
                    ans.append(i)
                    d[i] -= 1
        return ans






nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
nums1 = [1,2,2,1]
nums2 = [2,2]
nums1 = [1,2,3,4]
nums2 = [6,7,8,9]
print(Solution().intersect(nums1, nums2))