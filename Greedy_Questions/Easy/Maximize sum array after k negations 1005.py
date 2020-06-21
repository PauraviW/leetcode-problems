class Solution:
    def largestSumAfterKNegations(self, A: [], K: int) -> int:

        # A.sort()
        # for i in range(K):
        #     A[0]  = - A[0]
        #     A.sort()
        # sum = 0
        # for i in A:
        #     sum += i
        # return sum
        A = sorted(A)
        ncnt = sum([1 for a in A if a < 0])
        cnt1 = min(K, ncnt)
        cnt2 = K - ncnt if K > ncnt else 0
        for i in range(cnt1):
            A[i] = - A[i]
        return sum(A) - min(A) * 2 * (cnt2 % 2) if cnt2 else sum(A)


sol = Solution()
A = [2,-3,-1,5,-4]
K = 2
A = [3,-1,0,2]
K = 3
A = [4,2,3]
K = 1
print(sol.largestSumAfterKNegations(A, K))
