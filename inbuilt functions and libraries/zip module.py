
def zip1(*iterables):
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)
    #
    # for i in iterators:
    #     for j in i:
    #         print(j)

x = ['abc', 'def', 'ghij']

for i in zip(*x):
    print(i)
# y = [4, 5, 6]
# zipped = zip(x,y)

print(next(zip1(x)))