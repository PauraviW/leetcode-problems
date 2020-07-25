class Solution:
    def isHappy(self, n: int) -> bool:

        check_cycle = set()
        while True:
            sum = 0
            while n:
                sum += int(n % 10) ** 2
                print(sum)
                n = n // 10
            if sum == 1:
                return True
            elif sum in check_cycle:
                return False
            else:
                n = sum
                print(n)
                check_cycle.add(sum)

n = 19
print(Solution().isHappy(n))

