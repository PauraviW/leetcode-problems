def ugly_numbers(n):
    temp = 0
    while temp != n and n!= 1:
        temp = n
        if n%2 == 0:
            n = n //2
        if n%3 == 0:
            n = n //3
        if n%5 == 0:
            n = n //5
    return n
if ugly_numbers(7) == 1:
    print(True)
else:
    print(False)