s =  "Let's take LeetCode contest"
spl = s.split(' ')

for i in range(len(spl)):
    spl[i] = spl[i][::-1]

s = ' '.join(spl)
print(s)