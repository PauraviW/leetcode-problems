n = 499979
if n < 3:
    print(0)
primes = [True] * n
primes[0] = primes[1] = False
for i in range(2, int(n ** 0.5) + 1):
    if primes[i]:
        primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
print(sum(primes))