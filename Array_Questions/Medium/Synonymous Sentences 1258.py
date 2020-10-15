import heapq
import itertools
from collections import defaultdict, deque
synonyms =[["happy","joy"],["sad","sorrow"],["joy","cheerful"]]
text = "I am happy today but was sad yesterday"
# ans = set()
# ans.add(text)
# dic = defaultdict(str)
# graph=defaultdict(dict)
# bfs = deque()
# ans=set()
# bfs.append(text)
# for k,v in synonyms:
#     graph[k][v]=1
#     graph[v][k]=1
#
# while bfs:
#     curT=bfs.popleft()
#     ans.add(curT)
#     words=curT.split()
#     for i,w in enumerate(words):
#         if w in graph.keys():
#             for newW in graph[w]:
#                 newsent=' '.join(words[:i]+[newW]+words[i+1:])
#                 if newsent not in ans:
#                     bfs.append(newsent)
# # print(sorted(list(ans)))
# ["I am cheerful today but was sad yesterday",
#  "I am cheerful today but was sorrow yesterday",
#  "I am happy today but was sad yesterday",
#  "I am happy today but was sorrow yesterday",
#  "I am joy today but was sad yesterday",
#  "I am joy today but was sorrow yesterday"]

uf = {}


def union(x, y):
    uf[find(y)] = find(x)


def find(x):
    uf.setdefault(x, x)
    if uf[x] != x:
        uf[x] = find(uf[x])
    return uf[x]


for a, b in synonyms:
    union(a, b)
d = defaultdict(set)
for a, b in synonyms:
    root = find(a)
    d[root] |= set([a, b])
txt = text.split()
res = []
for t in txt:
    if t not in uf:
        res.append([t])
    else:
        r = find(t)
        res.append(list(d[r]))
fin_res = [" ".join(sentence) for sentence in itertools.product(*res)]
print(sorted(fin_res))