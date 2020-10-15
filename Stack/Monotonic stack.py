val = [8,6,4,5,7]


# increasing stack
firstSmallerToLeft = [-1]*len(val)
firstSmallerToRight = [-1]*len(val)
stack = []
for i in range(len(val)):
    if stack:
        if stack[-1] <= val[i]:
            firstSmallerToLeft[i] = stack[-1]
        else:
            while stack and stack[-1] > val[i]:
                n = stack.pop()
                firstSmallerToRight[val.index(n)] = val[i]
            if stack:
                firstSmallerToLeft[i] = stack[-1]
    stack.append(val[i])
print(firstSmallerToLeft, firstSmallerToRight)



val = [73, 74, 75, 71, 69, 72, 76, 73]
firstLargerToLeft = [0]*len(val)
firstLargerToRight = [0]*len(val)
stack = []
for i in range(len(val)):
    if stack:
        if val[stack[-1]] >= val[i]:
            firstLargerToLeft[i] = stack[-1]
        else:
            while stack and val[stack[-1]] < val[i]:
                n = stack.pop()
                firstLargerToRight[n] = i - n
            if stack:
                firstLargerToLeft[i] = stack[-1]
    stack.append(i)
print(firstLargerToRight)

