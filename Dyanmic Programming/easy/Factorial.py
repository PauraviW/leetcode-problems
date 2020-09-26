def factorial(n, dp):
    if n <= 1:
        return 1
    print(n)
    dp[n] = n * factorial(n-1, dp)
    return dp
dp = [0] * 11
print(factorial(10, dp))