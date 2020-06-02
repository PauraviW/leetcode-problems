s = "a0b1c2"
s = "leetcode"
s = "1229857369"
s = "covid2019"
s = "abc123"
alpha_count = 0
num_count = 0

alpha = []
nums = []
r = ""
for i in s:
    if i.isalpha():
        alpha_count += 1
        alpha.append(i)
    else:
        num_count +=1
        nums.append(i)
if  alpha_count == num_count or abs(alpha_count - num_count) == 1:
    if alpha_count > num_count:
        while len(nums) >0:
            r += alpha.pop(0)
            r+= nums.pop(0)

        r+=alpha.pop(0)
    elif alpha_count < num_count:
        while len(alpha) >0:
           r += nums.pop(0)
           r += alpha.pop(0)

        r+=nums.pop(0)
    else:
        while len(alpha) >0:
           r += nums.pop(0)
           r += alpha.pop(0)


else:
    print("")

print(r)

