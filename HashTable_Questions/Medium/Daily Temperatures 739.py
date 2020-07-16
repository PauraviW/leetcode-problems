class Solution:
    def dailyTemperatures(self, T: []) -> []:
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                prev_idx = stack.pop()
                ans[prev_idx] = i - prev_idx
            stack.append(i)

        return ans



T =  [73, 74, 75, 71, 69, 72, 76, 73]
# T = [89,62,70,58,47,47,46,76,100,70]
# T = [55,38,53,81,61,93,97,32,43,78]
print(T)
print(Solution().dailyTemperatures(T))






