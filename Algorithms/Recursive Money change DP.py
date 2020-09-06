class Solution:
    def recursive(self, money, coins):
        if money == 0:
            return 0
        min_num_coins = -1
        for i in range(len(coins)):
            if coins[i] <= money:
                print(money-coins[i], coins[i])
                num_coins =  self.recursive(money-coins[i], coins)
                if min_num_coins < 0 or num_coins + 1 < min_num_coins:
                    min_num_coins = num_coins + 1
        return  min_num_coins






money = 10
coins = [1, 5, 10, 25]

print(Solution().recursive(money, coins))
