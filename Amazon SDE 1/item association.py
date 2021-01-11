# Q1. Given a list of item association relationships, write an algorithm that outputs the largest item association group. If two groups have the same number of items then select the group which contains the item that appears first in lexicographic order.
#
# Input :
# [[Item1, Item2], [Item3, Item4], [Item4, Item5]]
#
# Output :
# [Item3, Item4, Item5]
from collections import defaultdict


class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited  = set()
    def largestItemAssociation(self, itemAssociation):
        for e1, e2 in itemAssociation:
            self.graph[e1].append(e2)
        max_len = 0
        ans = None
        for e in self.graph.keys():
             if e not in self.visited:
                self.visited.add(e)
                l = self.dfs(e, [e])
                if len(l) > max_len:
                    max_len = len(l)
                    ans = sorted(l)
                elif len(l) == max_len:
                    if sorted(l) < ans:
                        ans = sorted(l)
        return ans



    def dfs(self, curr, l=[]):
        if curr in self.graph:
            for nei in self.graph[curr]:
                if nei not in self.visited:
                    self.visited.add(nei)
                    l = self.dfs(nei, l + [nei])
        return l


obj = Solution()
print(obj.largestItemAssociation([["Item1", "Item2"], ["Item3", "Item4"], ["Item4", "Item5"], ["Item0","Item10"],["Item10", "Item23"]]))
