s = '[{}{()[{}]}]'

n = 0
while len(s) > 0 and n != len(s):
    n = len(s)
    for i in ('{}', '[]', '()'):
        s = s.replace(i, '')
        if len(s) < 1:
            break
print(s)