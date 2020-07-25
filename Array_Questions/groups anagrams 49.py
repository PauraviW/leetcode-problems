from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        dic = defaultdict(list)

        for i in strs:
            val = sorted(list(i))
            dic[''.join(val)].append(i)
        print(dic)




strs =  ["eat", "tea", "tan", "ate", "nat", "bat"]
strs = ['c','c']
strs = [""],
strs = ["", ""]
print(Solution().groupAnagrams(strs))