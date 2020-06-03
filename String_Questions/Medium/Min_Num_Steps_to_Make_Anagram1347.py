# s = "leetcode"
# t = "practice"
s = "anagram"
t = "mangaar"

# for i in s:
#     if i in t:
#         t = t.replace(i,'',1)
#         print(t)
# print(len(t))

### better solution ###

c = 0
for i in set(s):
    x = s.count(i) - t.count(i)
    if x > 0:
        c +=x
print(c)
  