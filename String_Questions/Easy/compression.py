atring = 'abaabbbc'
atring = 'abc'
atring = 'aab'
atring = 'wwww'
res = ''
i = 0
while i < len(atring):
    temp = 0
    while i + temp < len(atring) and atring[i + temp] == atring[i]:temp += 1
    res += atring[i]
    res += str(temp) if temp > 1 else ''
    i = i + temp

print(res)

