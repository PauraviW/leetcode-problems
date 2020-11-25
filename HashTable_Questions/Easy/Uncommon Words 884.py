A = "this apple is sweet"
B = "this apple is sour"
A = "apple apple"
B = "banana"
d = {}
for i in A.split(' '):
    d[i] = d.get(i, 0) + 1
for i in B.split(' '):
    d[i] = d.get(i, 0) + 1
print([key for key,value in d.items() if value==1])


import  collections
########### Better Solution ##########3
cnt = collections.Counter((A + ' ' + B).split(' '))
print([w for w, c in cnt.items() if c == 1])