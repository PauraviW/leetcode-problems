import re
s = 'ab-cd'
s = "a-bC-dEf-ghIj"
s = "Test1ng-Leet=code-Q!"
res1 = "".join(re.findall("[a-zA-Z]+", s))
res1 = res1[:: -1]
v= ''
k = 0
for i in range(len(s)):
    if s[i].isalpha():
        v +=res1[k]
        k += 1
    else:
        v += s[i]
print(v)


