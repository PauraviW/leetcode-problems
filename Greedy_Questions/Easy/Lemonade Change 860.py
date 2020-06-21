import collections
class Solution:
    def lemonadeChange(self, bills: []) -> bool:
        dic = collections.defaultdict(int)

        for i in bills:
            if i == 5:
                dic[5] = dic[5] + 1
            elif i == 10:
                if dic[5] < 1:
                    return False
                else:
                    dic[5] -= 1
                    dic[10] += 1
            else:
                if dic[10] > 0:
                    if dic[5] > 0:
                        dic[5] -=1
                        dic[10] -= 1
                    else:
                        return False
                else:
                    if dic[5] < 3:
                        return False
                    else:
                        dic[5] -= 3
        return True

                # dic[i]  = dic[i] + 1
                # difference = i - 5
                # if difference == 15:
                #     if dic[10] < 1 and dic[5] < 3:
                #         return False
                #     else:
                #         if dic[10] >= 1 and dic[5] >=1:
                #             dic[10] -= 1
                #             dic[5] -= 1
                #         elif dic[5] >=3:
                #             dic[5] -=3
                #         else:
                #             return False
                # elif difference == 5:
                #     if dic[5] < 1:
                #         return False
                #     else:
                #         dic[5] -= 1


bills = [5,5,5,10,20]
bills = [5,5,10]
bills = [10,10]
bills = [5,5,10,10,20]
sol = Solution()
print(sol.lemonadeChange(bills))


############## better in terms of time
five = ten = 0
for bill in bills:
    if bill == 5:
        five += 1
    elif bill == 10:
        five, ten = five - 1, ten + 1
    elif ten > 0:
        five, ten = five - 1, ten - 1
    else:
        five -= 3

    if five < 0:
        print(False)

print(True)