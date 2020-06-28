class Solution:
    def twoSum(self, numbers: [], target: int) -> []:

        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]



numbers = [2,7,11,15]
target = 9
sol = Solution().twoSum(numbers, target)
print(sol)
