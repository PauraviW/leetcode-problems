string = '0-2147483647'
op = '+'
string += '+'
stack = []
num = 0
for s in string:
    if s.isdigit():
        num = num*10 + int(s)
    elif s == ' ':
        continue
    else:
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            top = stack.pop()
            stack.append(num * top)
        elif op == '/':
            top = stack.pop()
            stack.append(top//num)
        num = 0
        op = s
print(sum(stack))