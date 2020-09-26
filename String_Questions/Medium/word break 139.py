import collections


class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
            queue = collections.deque()
            visited = set()
            queue.appendleft(0)
            visited.add(0)
            while len(queue) > 0:
                print('--------------------------------------------')
                curr_index = queue.pop()
                for i in range(curr_index, len(s) + 1):
                    print(s[curr_index:i])
                    if i in visited:
                        continue
                    if s[curr_index:i] in wordDict:
                        if i == len(s):
                            return True
                        queue.appendleft(i)
                        visited.add(i)
            return False

s = 'leetcode'
wordDict = ['leet', 'code']
print(Solution().wordBreak(s, wordDict))