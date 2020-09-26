def maxItems(v):

    n = len(v)
    count = [0] * (n+1)

    for x in v:
        count[min(x, n)] += 1

    size = 0
    size_arr = []
    ans = 0
    for k in range(1,n+1):
        while count[k] > 0 and size < k:

            size += 1

            ans += size
            count[k]-=1
        # print(k * count[k])
        size_arr.append(size)
        ans += k * count[k]

    return size_arr


def maxValue(arr):
    arr = sorted(arr)
    arr[0] = 1
    for i in range(1, len(arr)):
        if not (arr[i] < arr[i-1] + 2):
            arr[i] = arr[i-1] + 1
    return arr

v = [5, 2, 3, 7, 1, 2, 2]
print(maxItems(v))
print("maxVal", maxValue(v))

v = [3, 5, 1]
print(maxItems(v))
print("maxVal", maxValue(v))
v = [8, 1, 4, 0, 9, 4, 3, 2]
print(maxItems(v))
print("maxVal", maxValue(v))
v = [5, 1, 3, 4, 3, 3, 5]
print(maxItems(v))
print("maxVal", maxValue(v))

