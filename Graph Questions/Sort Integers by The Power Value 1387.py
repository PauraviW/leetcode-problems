from collections import defaultdict


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.dic = defaultdict(int)
        self.dic[1] = 0
        def power(x):
            if x in self.dic :
                return self.dic[x]
            if x % 2:
                self.dic[x] =  1 + power(3 * x + 1)
            else:
                self.dic[x] =  1 + power(x // 2)
            return self.dic[x]

        for i in range(lo, hi + 1):
            power(i)
        return sorted([i for i in range(lo, hi+1)], key = lambda x:(self.dic[x], x))[k-1]




lo = 7
hi = 11
k = 4
print(Solution().getKth(lo, hi, k))