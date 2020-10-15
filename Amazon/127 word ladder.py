import string
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        wordList = set(wordList)
        queue = deque()
        visited = set()
        queue.append(beginWord)

        changes = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return changes
                for j in range(len(word)):
                    for c in string.ascii_lowercase:
                        arr = list(word)
                        arr[j] = c
                        if ''.join(arr) in wordList and ''.join(arr) not in visited:
                            queue.append(''.join(arr))
                            visited.add(''.join(arr))
            changes += 1
        return 0
        # # def checkWord(curr, word):
        # #     diff = False
        # #     for c1, c2 in zip(curr, word):
        # #         if c1 != c2:
        # #             if diff:
        # #                 return False
        # #             else:
        # #                 diff = True
        # #     return True
        # #
        # # if not beginWord or not endWord or not wordList or endWord not in wordList:
        # #     return 0
        # # temp  = [beginWord]
        # # temp2 = []
        # # dic = defaultdict(set)
        # # count = 0
        # # while temp:
        # #     curr = temp.pop(0)
        # #     if curr == endWord:
        # #         return count + 1
        # #     for word in wordList:
        # #         if  checkWord(word, curr) and word not in dic :
        # #             temp2.append(word)
        # #             dic[curr].add(word)
        # #     if not temp:
        # #         temp2, temp = temp, temp2
        # #         count += 1
        # # return count
        # if not beginWord or not endWord or not wordList or endWord not in wordList:
        #     return 0
        # def checkWord(curr, word):
        #     diff = False
        #     for c1, c2 in zip(curr, word):
        #         if c1 != c2:
        #             if diff:
        #                 return False
        #             else:
        #                 diff = True
        #     return True
        #
        #
        # dic2 = defaultdict(set)
        # for i in wordList + [beginWord]:
        #     for j in wordList:
        #         if checkWord(i, j) and i != j:
        #             dic2[i].add(j)
        #
        # print(dic2)
        # temp = [beginWord]
        # temp2 = []
        # dic = defaultdict(set)
        # count = 0
        # flag = False
        # while temp:
        #     curr = temp.pop(0)
        #     if curr == endWord:
        #         flag = True
        #         return count + 1
        #     for word in wordList:
        #         if word in dic2[curr] and word not in dic:
        #             temp2.append(word)
        #             dic[curr].add(word)
        #     if not temp:
        #         temp2, temp = temp, temp2
        #         count += 1
        # return count + 1 if flag else 0


beginWord = "lost"
endWord = "miss"
wordList = ["most","mist","miss","lost","fist","fish"]
# print(Solution().ladderLength(beginWord, endWord, wordList))
print(Solution().ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))