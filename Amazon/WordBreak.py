class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        wordSet = set(wordDict)
        stack = [0]
        visited = set()
        while stack:
            curr = stack.pop()
            if curr == len(s):
                return True
            for j in range(curr, len(s)+1):
                if s[curr:j] in wordSet and j not in visited:
                    stack.append(j)
                    visited.add(j)
        return False
wordDict = ["leet","code"]
s = "leetcode"
print(Solution().wordBreak(s, wordDict))