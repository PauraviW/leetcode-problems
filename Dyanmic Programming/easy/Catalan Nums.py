from collections import defaultdict
def catalan(n):
    if catalan_nums[n]:
        return catalan_nums[n]
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n-1-i)
    return res
catalan_nums = defaultdict(int)
n = 100
for i in range(n):
    catalan_nums[i] = catalan(i)
print(catalan_nums.values())