class Solution:
    def finalPrices(self, prices: [int]) -> [int]:
        res = []
        for i in range(len(prices)):
            j = i + 1
            while j < len(prices) and prices[j] > prices[i]:
                j += 1
            if j < len(prices) and prices[i] - prices[j] >=0:
                res.append(prices[i] - prices[j])
            else:
                res.append(prices[i])
        return res


prices = [8,4,6,2,3]
print(Solution().finalPrices(prices))