import collections
s = "egg"
t = "add"
s = 'foo'
t = 'bar'
s = 'paper'
t = 'title'
if len(s) != len(t):
    print(False)
else:
    flag = True
    dic = collections.OrderedDict()
    for j in range(len(s)):
        if t[j] not in dic.keys() and s[j] not in dic.values():
            dic[t[j]] = s[j]
        else:
            if dic.get(t[j]) == s[j]:
                continue
            else :
                flag = False
                break

    if flag:
        print(True)
    else:
        print(False)
