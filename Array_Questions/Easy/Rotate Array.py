class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # rem = k
        # if k > len(nums):
        #     rem = k % len(nums)
        # d = dict()
        # for i, val in enumerate(nums):
        #     if i+rem >= len(nums):
        #         index = i + rem - len(nums)
        #     else:
        #         index = i + rem
        #     d[(i,index)] = val
        # for old, new in d.keys():
        #     nums[new] = d[(old, new)]
        # print(nums)
        toRotate = k % len(nums)
        rotated = []
        end = nums[len(nums) - toRotate:]
        print(end)
        beginning = nums[:len(nums) - toRotate]
        print(beginning)
        rotated = end + beginning
        for index in range(0, len(nums)):
            nums[index] = rotated[index]


nums = [1,2,3,4,5,6,7]
print(Solution().rotate(nums, 3))