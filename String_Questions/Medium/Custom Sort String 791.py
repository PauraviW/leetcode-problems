S = "zzzzzzzzzd"
T = "abcd"
l=''
for i in S:
    count = T.count(i)
    for j in range(count):
        l += i
    T = T.replace(i,'')

l+=T
print(l)
