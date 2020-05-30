# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:18:25 2020

@author: paura
"""
import math
max_zeros = 0
count = 0
# l1 = []
# start = 0
# for i in range(len(l)):
#     if l[i] == 1 and l[i+1]==0:
#         count+=1
#     if l[i] == 0:
#         count+=1
#     if l[i] == 0 and l[i+1] == 1:
#         count = 0
#
#
l = [1,1,0,0,0,1,0]
import re
# l = [1,0,0,0,1,0,1]
# l = [1,1,1,0,1,0,1,1,1,1,1,1,1,1,1]
# l = [1,0,0,0]
seats = [0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1]
consequentZero, ans = 0, 0
for s in seats:
    if s == 0:
        consequentZero += 1
        ans = max(ans, consequentZero)
    else:
        consequentZero = 0
ans = (ans + 1) // 2

print(max(ans, seats.index(1), seats[::-1].index(1)))