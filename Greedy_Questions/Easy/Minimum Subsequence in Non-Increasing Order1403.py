nums = [4,3,10,9,8, 0]
nums = [4,4,7,6,7]
nums = [6]
if len(nums) == 1 or len(set(nums)) == 1:
    print(nums)
while 0 in nums:
    nums.remove(0)
nums.sort(reverse = True)
print(nums)

for i in range(len(nums)):
    if sum(nums[:i+1]) > sum(nums[i+1:]):
        print(sum(nums[:i+1]), sum(nums[i+1:]), nums[i+1:], nums[:i+1])

        break


############## arrray slicing is a very heavy operation this use this instead

if len(nums) == 1:
            return nums
        sumNums = sum(nums)
        sumRes  = 0
        res     = []
        nums.sort(reverse = True)
        for idx, n in enumerate(nums):
            if sumNums >= sumRes:
                res.append(n)
                sumRes += n
                sumNums -= n
        return res