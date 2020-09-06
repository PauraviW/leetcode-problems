res = []


def addition(num1, num2):
    carry = 0
    res = []
    for i in range(len(num1)):
        result = int(num1[i]) + int(num2[i]) + carry

        if result > 9:
            carry = int(result / 10)
            result = result % 10
            res.append(str(result))
        else:
            carry = 0
            res.append(str(result))

    for j in range(i + 1, len(num2)):
        result = int(num2[j]) + carry
        if result > 9:
            carry = int(result / 10)
            result = result % 10
            res.append(str(result))
        else:
            carry = 0
            res.append(str(result))
    if carry > 0:
        res.append(str(carry))
    return ''.join(res[::-1])


num1 = "98"
num2 = "9"
num1 = num1[::-1]
num2 = num2[::-1]
if len(num1) < len(num2):
    print(addition(num1, num2))
else:
    print(addition(num2, num1))

