str1 = "{([])}"
str2 = "{]"

hashtable = {']':'[', '}': '{', ")":'('}
stack = []
for s in str2:
    if s in hashtable:
        top = stack.pop() if stack else '_'
        if top != hashtable[s]:
            print(False)
    else:
        stack.append(s)
if not stack:
    print(True)
else:
    print(False)
