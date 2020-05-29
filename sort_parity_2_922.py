# -*- coding: utf-8 -*-
"""
Created on Sun May 24 16:03:07 2020

@author: paura
"""

A = [4,2,5,7]

#l = []
#odd_numbers = []
#even_numbers = []
#for data in A:
#    if data%2 == 0:
#        even_numbers.append(data)
#    else:
#        odd_numbers.append(data)
#
#for i in range(len(A)):
#    if i%2==0:
#        l.append(even_numbers.pop())
#        
#    else:
#        
#        l.append(odd_numbers.pop())
#print(l)


            j = 1
            for i in range(0, len(A), 2):
                if A[i] % 2:
                    while A[j] %2:
                        j += 2
                    A[i], A[j] = A[j], A[i]
#return A