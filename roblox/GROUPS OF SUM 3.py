arr = [1.01, 1.01, 3, 2.7, 2.3, 1.99]
arr.sort()
left = 0
right = len(arr) - 1
count = 0
while left <= right:
    if left == right:
        count += 1
        break

    if arr[left] + arr[right] <= 3.0:
        left += 1
        right -= 1
        count += 1

    else:
        right -= 1
        count += 1

print(count)
