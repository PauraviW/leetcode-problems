class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)
        l = [[0]*(n+1) for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                print(text1[i-1], text2[j -1])
                if text1[i-1] == text2[j -1]:
                    l[i][j] = 1 + l[i-1][j-1]
                else:
                    l[i][j] = max(l[i-1][j], l[i][j - 1])
        print(l[m-1][j])
        print(l)

text1 = "abcde"
text2 = "ace"
print(Solution().longestCommonSubsequence(text1, text2))



















