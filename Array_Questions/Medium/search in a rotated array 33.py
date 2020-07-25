class Solution:
    def search(self, nums: [int], target: int) -> int:

        n = len(nums)
        lo = 0
        hi = n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

        rot = lo
        lo = 0
        hi = n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            realmid = (mid + rot) % n
            if nums[realmid] == target:
                return realmid
            if nums[realmid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
# nums = [3, 1]
target = 3
print(Solution().search(nums, target))
