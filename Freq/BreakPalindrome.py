import re

input = 'abbzzzzzbba'
i = 0
if input.count('a') == len(input):
    print ('IMPOSSIBLE')
else:
    while i < len(input) and input[i] == 'a':
        i += 1
    if i < len(input):
        input1 = input.replace( input[i], chr(ord(input[i]) - 1), 1)
    print(input1 < input, input1)
    print(ord('a'), chr(97))

if input == 'a' : print("IMPOSSIBLE")
if len(input) == '1': print('a')
for s in re.sub('[^a]', 'a', input, 1), input[:-1] + 'b':
    print(s, s[::-1], input)
    if s < s[::-1]:
        if s > input:
            print(s, input)
            print("IMPOSSIBLE")
        print(s)
