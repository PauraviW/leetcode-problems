s = 'abaccccaa'
m = [[0]* len(s) for i in range(len(s))]
for i in range(len(s)):
    for j in range(len(s)):
        if i == j:
            m[i][j] = 1
        elif j == i + 1 and j < len(s):
            if s[i:j+1]  == s[i:j+1][::-1]:
                print(s[i:j+1])
                m[i][j] = 1
max_d = 0
string = ''
for i in range(0,len(s)):
    for j in range(i+2, len(s)):
        if s[i] == s[j] and m[i+1][j-1] == 1:
            m[i][j] = 1
            if j - i + 1 > max_d:
                max_d = j - i + 1
                string = s[i:j+1]
print(string, max_d)