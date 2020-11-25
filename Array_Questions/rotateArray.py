def rotLeft(a, d):
    if d < len(a):
        return a[d:] + a[: d]
    else:
        act = len(a) % d
        print
        print(a[-act:], a[: len(a) - act])
        return a[-act:] + a[: len(a) - act]
print(rotLeft([1,2,3,4,5], 4))