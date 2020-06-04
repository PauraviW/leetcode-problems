left = 1
right = 22
l = []
for i in range(left, right+1):

    number = i
    flag = True
    if str(i).count('0') > 0:
        continue
    while i > 0:
        digit = int(i%10)
        if number%digit == 0:
            i = int(i / 10)
            continue
        else:
            flag = False
        i = int(i / 10)
    if flag:
        l.append(number)
print(l)









