n = 234
n = 4421

sum = 0
product = 1

while n > 0:
    sum+=int(n%10)
    product*=int(n%10)
    n = int(n/10)
print(sum, product, product-sum)