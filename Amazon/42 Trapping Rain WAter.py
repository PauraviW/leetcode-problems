class Solution:
    def trap(self, height: [int]) -> int:

        # max_l = {}
        # max_so_far = 0
        # for i in range(len(height)):
        #     if height[i] > max_so_far:
        #         max_so_far = height[i]
        #     max_l[i] = max_so_far
        # print(max_l)
        # max_r = {}
        # max_so_far = 0
        # for i in reversed(range(len(height))):
        #     if height[i] > max_so_far:
        #         max_so_far = height[i]
        #     max_r[i] = max_so_far
        #
        # total_water = 0
        # for i in range(len(height)):
        #     total_water += min(max_l[i], max_r[i]) - height[i]
        # print(total_water)



        # idea is that we need to check how much water can be stored at that particular block
        # we need to see by which towers is the area flagged from both sides.
        # that will give the highest amount that can be stored at each unit.
        # later we can subtract its height to get the actual units stored

        max_l = {}
        max_r = {}
        max_so_far = 0
        for i in range(len(height)):
            if height[i] > max_so_far:
                max_so_far = height[i]
            max_l[i] = max_so_far
        # likwise for right
        max_so_far = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] > max_so_far:
                max_so_far = height[i]
            max_r[i] = max_so_far

        # at each point the amount o water trapped is
        total = 0
        for i in range(len(height)):
            total += min(max_r[i], max_l[i]) - height[i]
        return total




height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
print(Solution().trap(height))
