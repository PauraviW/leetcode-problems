from collections import defaultdict
class Solution:
    def numSub(self, s: str) -> int:
        v = s.split('0')
        d = defaultdict(int)
        for i in v:
            if len(i) > 0:
                j = 0
s = "0110111"
print(Solution().numSub(s))