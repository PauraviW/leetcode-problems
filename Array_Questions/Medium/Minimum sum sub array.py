nums = [2,3,1,2,4,3]
s = 7
n = len(nums)
ans = float("inf")
left = 0
sum = 0
for i in range(n):
    sum += nums[i]
    while sum >= s:
        ans = min(ans, i + 1 - left)
        sum -= nums[left]
        left += 1

if ans != float("inf"):
    print(ans)
else:
    print(0)