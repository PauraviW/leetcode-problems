class Solution:
    def maxProfit(self, prices: []) -> int:
        if sorted(prices) == prices:
            return prices[-1] - prices[0]
        elif sorted(prices, reverse=True) == prices:
            return 0
        else:
            min_price = float("inf")
            max_price = 0

            for price in prices:
                min_price = min(price, min_price)
                profit = price - min_price
                max_price = max(max_price, profit)
            return max_price

prices =  [7,1,5,3,6,4]
print(Solution().maxProfit(prices))