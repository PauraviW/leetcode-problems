# paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
paths = [["B","C"],["D","B"],["C","A"]]
import collections
# paths = [["A","Z"]]
d = collections.defaultdict(list)

dic = collections.defaultdict(int)
for path in paths:
    dic[path[0]] = path[1]

key = list(dic.keys())[0]
print(dic)
while(dic.get(key, 0) != 0):
    key = dic[key]
print(key)