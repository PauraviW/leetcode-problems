
class Solution:
    def __init__(self):
        self.ans = 0
        self.priceOfJeans = [2, 3]
        self.priceOfShoes = [4]
        self.priceOfSkirts = [2, 3]
        self.priceOfTops = [1, 2]
        self.budget = 10
    def shoppingOptions(self, remainingAmount, currItem):

        if remainingAmount < 0:
            return
        if currItem == None:
            self.ans += 1
            return
        if currItem == 'Jeans':
            for price in self.priceOfJeans:
                if remainingAmount - price >= 0:
                    self.shoppingOptions(remainingAmount - price, "Shoes")
        elif currItem == 'Shoes':
            for price in self.priceOfShoes:
                if remainingAmount - price >= 0:
                    self.shoppingOptions(remainingAmount - price, "Skirts")
        elif currItem == 'Skirts':
            for price in self.priceOfSkirts:
                if remainingAmount - price >= 0:
                    self.shoppingOptions(remainingAmount - price, "Tops")
        elif currItem == 'Tops':
            for price in self.priceOfTops:
                if remainingAmount - price >= 0:
                    self.shoppingOptions(remainingAmount - price, None)


    def findOptions(self):
        self.shoppingOptions(self.budget, "Jeans")
        return self.ans

print(Solution().findOptions())



