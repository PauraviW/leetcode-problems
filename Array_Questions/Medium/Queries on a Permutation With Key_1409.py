m = 9
queries = [2,2,2,2, 2]
p = [i+1 for i in range(m)]
l = []
for  i in queries:
    l.append(p.index(i))
    p.remove(i)
    p.insert(0,i)
print(p,l)