
A = [2,0,6]
K = 806

i = len(A) - 1
while i >= 0 and K > 0:
    _sum = A[i] + K
    A[i] = _sum%10
    K =  _sum// 10
    i -= 1
print(A, _sum)
while K>0:
    A.insert(0, K%10)
    K = K//10
print(A)
 


