nums = [2,2,3, 1]
########################################## My solution
# print(nums)
# nums.remove(max(nums))
# print(nums)
# nums.remove(max(nums))
# print(nums)
#######################################

########################### Better Solution
a = b = c = -float("inf")
for n in nums:
    if n in (a, b, c): continue
    if n > a: n, a = a, n
    if n > b: n, b = b, n
    if n > c: n, c = c, n
print (a if c == -float("inf") else c)

#######################################333