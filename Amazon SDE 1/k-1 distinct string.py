# # Given a string s, and a const k, return all substrings of length k such that there are k-1 distinct characters in each substring.
# Input :
# S = "awaglk", k = 4
#
# Output :
# [awag]
#
# Explanation :
# All possible substrings of length k from the given string are [awag, wagl, aglk]. And only "awag" has k-1 distinct characters.


class Solution:
    def subStringsLessKDist(self, inputstring, k):
        if not inputstring:
            return []
        ans = []
        numDist = 0
        countdict = {i:0 for i in set(list(inputstring))}
        left = 0
        right = 0

        while left < len(inputstring) and right < len(inputstring):

            countdict[inputstring[right]] += 1
            if countdict[inputstring[right]] == 1:
                numDist += 1

            if right - left + 1 == k:
                if numDist == k-1:
                    ans.append(inputstring[left:right+1])
                countdict[inputstring[left]] -= 1
                if countdict[inputstring[left]] == 0:
                    numDist -= 1
                left += 1

            else:
                right += 1
        return ans





obj = Solution()
print(obj.subStringsLessKDist('awagalkk', 1))