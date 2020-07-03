from collections import defaultdict
class Solution:
    def convertTodecimal(self, arr):
        val = []
        for i in arr:
            k = 0
            num = 0
            for j in i[::-1]:
                num += int(j)*(2**k)
                k+=1
            val.append(num)
        return val
    def sortByBits(self, arr: []) -> []:
        d = defaultdict(list)

        for i in arr:
            a = sum(list(map(int, list(bin(i)[2:]))))
            d[a].append(i)
        val = []
        for i in sorted(d.keys()):
            val += sorted(d[i])
        return val






arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# arr = [1024,512,256,128,64,32,16,8,4,2,1]
# arr = [10000,10000]
# arr = [2,3,5,7,11,13,17,19]
print(arr)
print(Solution().sortByBits(arr))