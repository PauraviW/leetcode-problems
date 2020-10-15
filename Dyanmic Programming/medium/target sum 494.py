class Solution:
    def findTargetSumWays(self, nums: [int], S: int) -> int:

        self.count = 0
        self.memo = {}
        def traverse(index, currSum):
            if (index, currSum) in self.memo:
                return self.memo[(index, currSum)]

            if currSum == S and index == len(nums):
                self.count += 1
                return 1
            if index >= len(nums):
                return 0


            positive = traverse(index + 1, currSum + nums[index])

            negative = traverse(index + 1, currSum - nums[index])
            self.memo[(index, currSum)] = positive + negative
            return positive + negative


        return traverse(0, 0)

S = 3
nums= [1, 1, 1, 1, 1]
print(Solution().findTargetSumWays(nums, S))