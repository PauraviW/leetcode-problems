S = "aabababab"
temp = 0
l = [i*2 for i in set(list(S))]
while temp != len(S):
    temp = len(S)
    for i in l:
        S = S.replace(i, '')
print(S)
