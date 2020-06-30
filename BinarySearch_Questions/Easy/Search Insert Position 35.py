class Solution:
    def searchInsert(self, nums: [], target: int) -> int:
        low = 0
        high = len(nums) - 1
        return self.bsearch(nums, low, high, target)


    def bsearch(self, nums, low, high, target):
        if low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return  self.bsearch(nums, low, mid - 1, target)
            else:
                return self.bsearch(nums, mid+1, high, target)
        else:
            return low

nums = [1,3,5,6]
target = 5
nums = [1,3,5,6]
target = 2
nums = [1,3,5,6]
target = 7
nums = [1,3,5,6]
target = 0
solution = Solution().searchInsert(nums, target)
print(solution)



