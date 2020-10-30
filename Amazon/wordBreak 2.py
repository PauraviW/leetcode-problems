class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> [str]:
        self.ans = []
        self.dict = {}

        def dfs(s):
            if s in self.dict:
                return self.dict[s]
            result = []
            for word in wordDict:
                if s[:len(word)] == word:
                    if len(word) == len(s):
                        result.append(word)
                        # return result
                    else:

                        temp = dfs(s[len(word):])
                        for t in temp:
                            result.append(word + ' ' + t)
            self.dict[s] = result

            return result

        return dfs(s)

