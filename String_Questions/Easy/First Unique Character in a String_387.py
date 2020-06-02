s = "leetcode"
s = "loveleetcode"
s = "aabbcc"
# d = {}
# for i in s:
#     d[i] = d.get(i, 0) + 1
#
# min_ind = 99999
# char = ''
# for key, value in d.items():
#     if d[key] == 1:
#         if s.index(key) < min_ind:
#             min_ind =  s.index(key)
#             char = key
# if min_ind == 99999:
#     print(-1)
# print(char, min_ind)

############### better implementation

seen = set()
for char in s:
    if char not in seen and s.count(char) == 1:
        print(s.index(char))
    seen.add(char)

print(-1)