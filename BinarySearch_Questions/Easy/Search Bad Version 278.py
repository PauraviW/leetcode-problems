class Solution:
    def __init__(self, n):
        self.startBadVersion = n
    def isBadVersion(self, version):
        if version >= self.startBadVersion:
            return True
        else:
            return False

    def bsearch(self, n, low, high):
        if low <= high:
            mid = (low + high) // 2
            if self.isBadVersion(mid):
                if self.isBadVersion(mid - 1) == False:
                    return mid
                return self.bsearch(n, low, mid - 1)
            else:
                return self.bsearch(n, mid + 1, high)
        else:
            return -1
    def firstBadVersion(self, n):
        low = 1
        high = n
        return self.bsearch(n, low, high)

print(Solution(2).firstBadVersion(2))