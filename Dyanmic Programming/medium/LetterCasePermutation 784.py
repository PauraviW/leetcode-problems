from collections import defaultdict


class Solution:
    def letterCasePermutation(self, S: str) -> [str]:
        self.ans = []
        self.memo = defaultdict(list)

        def traverse(curr_index, ss):
            if curr_index == len(S) :
                self.ans.append(ss)
                return ss

            if S[curr_index].isalpha():
                traverse(curr_index + 1, ss + S[curr_index])
                traverse(curr_index + 1, ss + S[curr_index].upper())
            else:
                traverse(curr_index + 1, ss + S[curr_index])

        traverse(0, '')
        print(self.ans)


S = '3Z4'
S = "a1b2"
print(Solution().letterCasePermutation(S.lower()))