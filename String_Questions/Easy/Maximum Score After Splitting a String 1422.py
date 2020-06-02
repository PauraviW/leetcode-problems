s = "011101"
s = "00111"
s = "1111"
s = "0000"
max_score = 0
for i in range(len(s)):
    print(s[0:i+1], s[i+1:])
    if len(s[0:i+1]) > 0 and len(s[i+1:]) > 0:
        left = s[0:i+1].count('0')
        right = s[i+1:].count('1')
        if left + right > max_score:
            max_score = left + right
print(max_score)