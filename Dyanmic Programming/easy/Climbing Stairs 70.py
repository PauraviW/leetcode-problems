from collections import defaultdict

class Solution:
    def climbStairs(self, n: int) -> int:
        pathSoFar = []
        self.mainPath = defaultdict(int)


        self.calculatePath(n, 1, pathSoFar)
        pathSoFar = []

        self.calculatePath(n, 2, pathSoFar)
        print(self.mainPath)
        return len(self.mainPath)

    def calculatePath(self, n, start_index, pathSoFar):
        if start_index > n:
            pathSoFar = []
            return
        if start_index == n:
            if tuple(pathSoFar) not in self.mainPath:
                self.mainPath[tuple(pathSoFar)] += 1
            if pathSoFar:
                pathSoFar.pop()
            return
        else:
            pathSoFar.append(start_index)

        self.calculatePath(n, start_index + 1, pathSoFar)

        self.calculatePath(n, start_index + 2, pathSoFar)

n = 4

print(Solution().climbStairs(n))