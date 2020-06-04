n = 1010

a = 0
b = 0
while str(a).count('0') > 0 or str(b).count('0') > 0:
    a += 1
    b = n - a

print([a,b])