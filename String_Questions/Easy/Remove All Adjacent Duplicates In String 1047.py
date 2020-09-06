class Solution:
    def removeDuplicates(self, S: str) -> str:
        n = 0
        while True:
            n = len(S)
            for i in range(len(S) - 1):
                if S[i] == S[i+1]:
                    S = S.replace(S[i:i+2], "")
                    break
            if len(S) == n:
                break
        return S
import string
string.ascii_lowercase

S = "abbaca"
S = 'asdfghj'
S = ''
S= 'aabbcc'
S = "cabbac"
print(Solution().removeDuplicates(S))