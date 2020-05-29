# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 19:21:59 2019

@author: paura
"""


class Solution:
    def twoSum(self, nums , target) :
         
            #nums.sort()
            for i in range(len(nums)):
                print(i)
                diff = target - nums[i]
                print(diff)
                
                if diff in nums:
                    if nums.index(diff) != i:
                        v = [nums.index(diff),i]
                        v.sort()
                        return v
                    

s = Solution()
print(s.twoSum([3,2,4],6)) 