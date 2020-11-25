def count(number):
    t = 0
    print(number)
    while number:
        number = number & (number-1)
        print(number)
        t += 1
    print("count", t)
    return t

add = 0
total = 2**3

for i in range(2**3):
    if count(i) % 2 == 0:
        add+= 1
probability = add/total
print(probability)
