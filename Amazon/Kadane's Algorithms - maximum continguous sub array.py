a = [10,2,3,-10,5,10,2,-10,6]

max_end = 0
max_sum_so_far = 0
end = start = s = 0

for i in range(len(a)):
    max_end = max_end + a[i]

    if max_end > max_sum_so_far:
        max_sum_so_far = max_end
        start = s
        end = i
    if max_end < 0:
        s = s + 1
        max_end = 0
print(max_sum_so_far, start, end)
