# Given a circular array (the next element of the last element is the first element of t
# he array), print the Next Greater Number for every element. The Next Greater Number of a number
# x is the first greater number to its traversing-order next in the array, which means you could
# search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

a  = [1,1,3,2,4,2,1]
ans = [-1]* len(a)
stack = []
for i in range(2*len(a)):
    while stack and a[stack[-1]] < a[i%len(a)]:
        n = stack.pop()
        ans[n] = a[i%len(a)]
    stack.append(i%len(a))
print(ans)
