arr = [1,1,3,5,5, 5]
target = 0
def binarySearch(left, right, row):

    if left < right:
        mid = left + (right - left)//2
        if row[mid] >target:
            right = mid
        else:
            left = mid + 1
        return binarySearch(left, right, row)
    else:
        return left
print(binarySearch(0, len(arr), arr))