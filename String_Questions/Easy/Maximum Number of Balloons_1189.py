
import collections
text = text = "balloon"
d = collections.defaultdict()
for i in text:
    if i in ['b','a','l','o','n']:
        d[i] = d.get(i,0) + 1
count = 0
while d.get('b',0) > 0 and  d.get('a',0) > 0 and d.get('l',0) > 1 and d.get('o',0) > 1 and d.get('n',0) > 0:
    d['b'] -=1
    d['a'] -= 1
    d['l'] -= 2
    d['o'] -= 2
    d['n'] -= 1
    count += 1
print(count)


###better implementation

from collections import Counter

counter = Counter(text)
print(counter)
b = counter['b']
a = counter['a']
l = counter['l'] // 2
o = counter['o'] // 2
n = counter['n']

print(min(b, a ,l, o, n))