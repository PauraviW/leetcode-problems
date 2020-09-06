class Solution:
    def canJump(self, nums: [int]) -> bool:
        # some primitive cases
        if len(nums) == 1:
            return True
        return self.can_jump_recursive(nums, start_index = 0)

    def can_jump_recursive(self, nums, start_index = 0):

        # positive case
        if start_index == len(nums) - 1:
            return True
        # beyond the array
        if start_index > len(nums) - 1:
            return False
        # in between but cannot move forward
        if start_index < len(nums) - 1 and nums[start_index] == 0:
            return False
        canStop = False
        for i in range(1, nums[start_index]+1):
            canStop = self.can_jump_recursive(nums, start_index + i)
            if canStop:
                return True
        return canStop


nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]
print(Solution().canJump(nums))
