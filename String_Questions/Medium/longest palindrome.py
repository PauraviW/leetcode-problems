class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ''
        self.resLen = 0

        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if self.resLen < r - l + 1:
                    self.resLen = r - l + 1
                    self.res = s[l: r + 1]

                l -= 1
                r += 1
            print(self.resLen, self.res)

            # return self.res, resLen

        for i in range(len(s)):

            # odd
            l, r = i, i
            helper(l, r)
            # even
            l, r = i, i + 1
            helper(l, r)

        return self.res


s = 'ab'

print(Solution().longestPalindrome(s))








