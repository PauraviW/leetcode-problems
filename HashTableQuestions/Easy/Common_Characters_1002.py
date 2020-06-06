import collections
A = ["bella","label","roller"]
A = ["cool","lock","cook"]

d = collections.defaultdict(list)
for i in A[0]:
    if i not in d:
        d[i].append(A[0].count(i))
print(d)
for word in A[1:]:
    for letter in set(word):
        if letter in d:
            d[letter].append(word.count(letter))
print(d)
l = []
for key, value in d.items():
    if len(value) == len(A):
        count = min(value)
        while count!=0:
            l.append(key)
            count -= 1
print(l)
