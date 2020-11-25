nums1 = [1,2,2,1]
nums2 = [2,2]
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
l = []
import  collections

d = collections.defaultdict(int)

for i in nums1:
    d[i] = d.get(i, 0) + 1
print(d)

for i in nums2:
    if d[i] != 0:
        l.append(i)
        d[i] -= 1
print(l)