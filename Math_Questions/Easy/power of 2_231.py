n = 64
if n == 1: print(True)
print(n and not (n & (n - 1)))
while n % 2 == 0:
    n = n / 2
    print(n)
if n == 1:
    print(True)
else:
    print(False)


