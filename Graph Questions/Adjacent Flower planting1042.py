from collections import defaultdict


class Solution:
    def gardenNoAdj(self, N: int, paths: [[int]]) -> [int]:
        gd = defaultdict(set)
        res = defaultdict(set)
        for s, t in paths:
            gd[s].add(t)
            gd[t].add(s)

        for g, c in gd.items():

            for i in [1,2,3,4]:
                comm = res[i] & c
                if not comm:
                    res[i].add(g)
                    break
        ans = [1]*N
        for k, v in res.items():
            for i in v:
                ans[i-1] = k


        return ans
N = 4
paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
# paths = [[1,2],[3,4]]
# N = 3
# paths = [[1,2],[2,3],[3,1]]
N = 1
paths = []
N = 0
paths = []
print(Solution().gardenNoAdj(N, paths))