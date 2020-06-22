class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        v = False
        while i < len(t) and len(s) > 0:
            if t[i] == s[0]:
                s = s[1:]
            i = i + 1
        if len(s) > 0:
            return False
        else:
            return True





s = 'abc'
t = 'ahbgdc'
s = "axc"
t = "ahbgdc"
sol = Solution().isSubsequence(s, t)
print(sol)

