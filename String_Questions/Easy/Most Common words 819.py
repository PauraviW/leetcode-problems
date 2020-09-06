import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: [str]) -> str:
        s = set(banned)
        print("".join((char if char.isalpha() else " ") for char in paragraph).split())
        word = ""
        l = []
        for i in paragraph.lower():
            if i.isalpha():
                word += i
            else:
                if len(word)> 0:
                    l.append(word)
                word = ''
        if len(word) > 0:
            l.append(word)
        from math import log10
        print(log10(27)/log10(3) % 1 == 0)
        record = collections.Counter(l)
        freq = sorted(record.keys(), key = lambda n: record[n], reverse= True)
        # for i in freq:
        #     if i not in s:
        #         return i







paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
# paragraph = "a, a, a, a, b,b,b,c, c"
# banned = ["a"]

print(Solution().mostCommonWord(paragraph,banned))