from collections import defaultdict


class Solution:
    def canBeEqual(self, target: [], arr: []) -> bool:
        d = defaultdict(int)

        for i in target:
            d[i] += 1

        for i in arr:
            d[i] -= 1
        return len(set(d.values())) == 1 and list(set(d.values()))[0] == 0


target = [1,2,3,4]
arr = [2,4,1,3]
# target = [7]
# arr = [7]
# target = [1,12]
# arr = [12,1]
# target = [3,7,9]
# arr = [3,7,11]
print(Solution().canBeEqual(target, arr))

