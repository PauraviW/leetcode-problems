class Solution:
    def findUnsortedSubarray(self, nums: []) -> int:

        sorted_array = sorted(nums)
        L = len(nums)
        for i in range(L):
            if nums[i] != sorted_array[i]:
                low = i
                break

        for i in reversed(range(L)):
            if nums[i] != sorted_array[i]:
                high = i
                break
        return high - low + 1




val = [2, 6, 4, 8, 10, 9, 15]
print(Solution().findUnsortedSubarray(val))

