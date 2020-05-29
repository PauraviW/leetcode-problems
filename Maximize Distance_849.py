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
# l = [1,1,0,0,0,1,0]
l = [1,0,0,0]
l = [0,1,1,1,0,0,1,0,0]
for i, data in enumerate(l):
    if data == 0:
        count += 1

        if count > max_zeros:
            max_zeros = count
            start = i - max_zeros + 1
    if data == 1:
        if count > max_zeros:
            max_zeros = count
            start = i - max_zeros + 1
        count = 0


if start == 0:
    index = start
elif start + max_zeros == len(l):
    index = len(l) - 1
else:
    index = start + (max_zeros)//2
dist1 = 0


# l = [1,1,0,0,0,1,0]
# [0,1,1,1,0,0,1,0,0]
print(max_zeros, start, len(l), index)
for i in range(index+1, len(l)):
    print(i, l[i],dist1, "order")
    if  l[i] == 0:
        dist1 +=1
    if l[i] == 1:
        dist1 += 1
        break
dist2 = 0
for i in reversed(range(0,index)):

    if l[i] == 0:
        dist2 += 1
    if l[i] == 1:
        dist2 += 1
        break
print(dist1, dist2)
    # return start
