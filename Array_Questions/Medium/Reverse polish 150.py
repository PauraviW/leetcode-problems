tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# tokens = ["4", "13", "5", "/", "+"]
# tokens = ["2", "1", "+", "3", "*"]
import operator
ops = { "+": operator.add, "-": operator.sub, '*':operator.mul, "/":operator.truediv }
i = 0
total = 0
value = 0

# while len(tokens)>1:
#     while i < len(tokens) and tokens[i].lstrip('-').isnumeric():
#         i += 1
#     val1 = int(tokens[i - 2])
#     val2 = int(tokens[i - 1])
#     total = int(ops[tokens[i]](val1, val2))
#     del tokens[i]
#     del tokens[i-1]
#     tokens[i-2] = str(total)
#     i = i - 2
#     print(tokens)
# print(tokens[0])

# better solution

stack = []

for c in tokens:
    if c not in '+/*-':
        stack.append(c)
    else:
        val2 = int(stack.pop())
        val1 = int(stack.pop())

        if c == '+':
            stack.append(val1+val2)
        elif c == '-':
            stack.append(val1-val2)
        elif c == '*':
            stack.append(val1*val2)
        else:
            stack.append(val1/val2)
print(stack[0])
