from collections import OrderedDict
# words = ["abc","deq","mee","aqq","dkd","ccc"]
# pattern = "abb"
words= ["badc","abab","dddd","dede","yyxx"]
pattern = "baba"
l = []

for i in words:
    flag = True
    if len(i) != len(pattern):
        flag = False
        continue
    else:
        dic = OrderedDict()
        for j in range(len(i)):
            if pattern[j] not in dic.keys() and i[j] not in dic.values():
                dic[pattern[j]] = i[j]
            else:
                if dic.get(pattern[j])  == i[j]:
                    continue
                else:
                    flag = False
                    break
        if flag:
            l.append(i)

print(l)


################################### better solution in terms of time
res = []
#
#
# def match(word, pattern):
#     if len(word) != len(pattern):
#         return False
#     dir = {}
#     for w, p in zip(word, pattern):
#         if w not in dir:
#             if p in dir.values():
#                 return False
#             dir[w] = p
#         else:
#             if dir[w] != p:
#                 return False
#     return True
#
#
# for w in words:
#     if match(w, pattern):
#         res.append(w)
# return res

#################################33









