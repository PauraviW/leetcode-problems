# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:25:20 2020

@author: paura
"""
import numpy as np
def oddCells(n, m, indices) :
        initial_matrix = np.zeros((n,m))
        
        for row, col in indices:
            initial_matrix[row,:] += 1
            initial_matrix[:, col] += 1
        print(initial_matrix)
        return np.where(initial_matrix%2!=0)[0].shape[0]
        
n = 3
m = 2
indices = [[0,1],[1,1]]
print(oddCells(n, m, indices))

odd_count = 0
rows = [0] * n
cols = [0] * m

for i, j in indices:
	rows[i] = rows[i] ^ 1
	cols[j] = cols[j] ^ 1

for i in range(n):
	for j in range(m):
		if(rows[i] ^ cols[j] == 1): odd_count += 1