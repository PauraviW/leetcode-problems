class Solution:
    def maxProfit(self, prices: []) -> int:
        if sorted(prices) == prices:
            return prices[-1] - prices[0]
        if sorted(prices, reverse=True) == prices:
            return 0

        i = 0
        L = len(prices)
        profit = 0
        current = 0
        b = False
        while i < L - 1:
            while i < L - 1 and prices[i] >= prices[i+1] :
                i = i + 1
            bought = prices[i]
            bI = i
            while  i < L - 1 and prices[i] <= prices[i+1]:
                i = i + 1
            if i == bI:
                return profit
            sell = prices[i]
            profit += sell - bought
            i = i + 1
        return profit



            # else:
            #     current = prices[i]
            #     while i < L - 1 and prices[i+1] > prices[i]:
            #         i = i + 1
            #     profit += prices[i] - current



sol = Solution()
arr = [7,1,5,3,6,4]
arr = [1,2,3,4,5]
arr = [7,6,4,3,1]
arr = [5,8, 1,1 ,1 ,1]
print(sol.maxProfit(arr))

