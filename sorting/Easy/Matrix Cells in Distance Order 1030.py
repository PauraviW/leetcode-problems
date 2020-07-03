from collections import defaultdict
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> [[]]:
        return sorted(lambd)
        # d = defaultdict(list)
        # for row in range(R):
        #     for col in range(C):
        #         d[abs(row - r0) + abs(col - c0)].append([row, col])
        # val = []
        # for i in sorted(d.keys()):
        #     val += d[i]
        # return  val
        #







# R = 1, C = 2, r0 = 0, c0 = 0
#  R = 2, C = 3, r0 = 1, c0 = 2
print(Solution().allCellsDistOrder( R = 2, C = 3, r0 = 1, c0 = 2))

️️