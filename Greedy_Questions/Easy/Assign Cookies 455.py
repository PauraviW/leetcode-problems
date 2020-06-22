class Solution:
    def findContentChildren(self, g: [], s: []) -> int:
        g.sort(reverse = True)
        s.sort(reverse = True)
        count = 0
        for i in range(len(g)):
            if len(s) > 0 and s[0] - g[i] >= 0:
                count += 1
                s.pop(0)
        return count



g = [1,2,3]
s = [1,1]
# g = [1,2]
# s = [1,2,3]
# g = [1,2,3]
# s = [3]
g = [10,9,8,7]
s = [5,6,7,8]


sol = Solution()
print(sol.findContentChildren(g, s))
