class Solution:
    def trap(self, height: [int]) -> int:

        max_l = {}
        max_so_far = 0
        for i in range(len(height)):
            if height[i] > max_so_far:
                max_so_far = height[i]
            max_l[i] = max_so_far
        print(max_l)
        max_r = {}
        max_so_far = 0
        for i in reversed(range(len(height))):
            if height[i] > max_so_far:
                max_so_far = height[i]
            max_r[i] = max_so_far

        total_water = 0
        for i in range(len(height)):
            total_water += min(max_l[i], max_r[i]) - height[i]
        print(total_water)


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))
