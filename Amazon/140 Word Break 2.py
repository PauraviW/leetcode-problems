from collections import deque, defaultdict


class Solution:
    def wordBreak(self, s, wordDict):

        # we have break the word and send the rest of the string recursivlely to this funvtion
# this will check if the start of the eord matched the word in the dictionary.
        dic = {}

        # def wb(s):
        #     if s in dic:
        #         return dic[s]
        #     result = []
        #
        #     for word in wordDict:
        #         if s[:len(word)] == word:
        #             if len(s) == len(word):
        #                 result.append(word)
        #             else:
        #                 temp = wb(s[len(word):])
        #                 for t in temp:
        #                     result.append(word + ' ' + t)
        #     dic[s] = result
        #     return result
        #
        # return wb(s)

        dp = {}

        def word_break(s):
            if s in dp: return dp[s]
            result = []
            for w in wordDict:
                if s[:len(w)] == w:
                    if len(w) == len(s):
                        result.append(w)
                    else:
                        tmp = word_break(s[len(w):])
                        for t in tmp:
                            result.append(w + " " + t)
            dp[s] = result
            return result

        return word_break(s)

s, wordDict = "catsanddog",["cat","cats","and","sand","dog"]
s, wordDict = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print("gfg", Solution().wordBreak(s, wordDict))

# a = ["a a a a a a a","aa a a a a a","a aa a a a a","a a aa a a a","aa aa a a a","aaaa a a a","a a a aa a a","aa a aa a a","a aa aa a a","a aaaa a a","a a a a aa a","aa a a aa a","a aa a aa a","a a aa aa a","aa aa aa a","aaaa aa a","a a aaaa a","aa aaaa a","a a a a a aa","aa a a a aa","a aa a a aa","a a aa a aa","aa aa a aa","aaaa a aa","a a a aa aa","aa a aa aa","a aa aa aa","a aaaa aa","a a a aaaa","aa a aaaa","a aa aaaa"]
# b = ["a aa aaaa","aa a aaaa","a a a aaaa","a aaaa aa","aaaa a aa","aa aa a aa","a a aa a aa","a aa aa aa","aa a aa aa","a a a aa aa","aa aaaa a","a a aaaa a","aaaa aa a","aa aa aa a","a a aa aa a","a aaaa a a","aaaa a a a","aa aa a a a","a a aa a a a","a aa aa a a","aa a aa a a","a a a aa a a"]
print
# print(set(a) - set(b))
# print(set(b) - set(a))