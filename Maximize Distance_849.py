# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:18:25 2020

@author: paura
"""
import math
l = [1,0,0,0]
max_zeros = 0
count = 0
l1 = []
start = 0
for i in range(len(l)):
    if l[i] == 1 and l[i+1]==0:
        count+=1
    if l[i] == 0:
        count+=1
    if l[i] == 0 and l[i+1] == 1:
        count = 0
        
 