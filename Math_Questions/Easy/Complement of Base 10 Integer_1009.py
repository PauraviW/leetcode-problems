n = 10
bn = bin(n)
bn_complement = ''
for i in bn[2:]:
    if i == '0':
        bn_complement +='1'
    else:
        bn_complement += '0'
print(int('0b'+bn_complement, 2))


