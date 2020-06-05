import string
letters = string.ascii_uppercase
num = 1377
s = ''
#
# if n< 26:
#     print(letters[n-1])
# while n >= 1:
#     rem = int(n%26)
#     print("rem", rem)
#     if rem == 0:
#         s+='Z'
#     else:
#         s+=letters[rem-1]
#     n = int(n/26)
#     print(n, s)
# if n!=0:
#     s+=letters[n-1]
# print(s)

capitals = list(letters)
result = []
while num > 0:
    result.append(capitals[(num - 1) % 26])
    print((num - 1) % 26, capitals[(num - 1) % 26])
    num = (num - 1) // 26
result.reverse()
print(''.join(result))