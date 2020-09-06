class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) <= 0:
            return True
        if len(s) > 0 and len(t) <= 0:
            return False
        if len(set(list(s)) - set(list(t))) > 0:
            return False
        if s[0] == t[0]:

            return self.isSubsequence(s[1:], t[1:])
        else:
            return self.isSubsequence(s, t[1:])


s = 'abc'
t = 'ahbgdc'
print(Solution().isSubsequence(s, t))