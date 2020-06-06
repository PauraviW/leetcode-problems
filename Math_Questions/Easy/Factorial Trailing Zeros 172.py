count = 0

from math import factorial
print(factorial(10))
def trailing_zeros(n):
    print(n, int(n/5))
    return 0 if n==0 else int(n/5) + trailing_zeros(int(n/5))

n = trailing_zeros(10)
print(n)
