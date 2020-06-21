class Solution:
    def lastStoneWeight(self, stones: []) -> int:
        stones.sort(reverse = True)

        while len(stones) > 1:
            diff = stones[0] - stones[1]
            stones.pop(0)
            stones.pop(0)
            if diff > 0:
                stones.append(diff)
                stones.sort(reverse=True)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
    def new(self, stones):
        while len(stones) > 1:
            stones.sort()
            print(stones)
            x, y = stones[-2:]
            if x == y:
                stones = stones[:-2]
            else:
                stones = stones[:-2] + [y - x]

        if not stones:
            return 0
        else:
            return stones[0]

stones = [2,7,4,1,8,1]
stones = [2,1,1,1,1,1]
stones = [5]

sol = Solution()
print(sol.lastStoneWeight(stones))


##################### Same technique but precise

