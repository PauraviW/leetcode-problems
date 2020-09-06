class Solution:
    def kthGrammar(self, N: int, k: int) -> int:
        d = {'0':'01', '1':'10'}
        s = '01'
        # if N == 1:
        li = ['0','01']
        for i in range(1, N):
            l = len(s)//2
            t = d[s[:l]]
            v = ''
            if d.get(s[l:], -1) != -1:
                v += d[s[l:]]
            else:
                x = s[l:]
                l1 = len(x)//2
                v += d[x[:l1]] + d[x[l1:]]
                d[x] = v
            d[s] = t + v

            s = t + v
            li.append(s)
        print(li)
        return li[N-1][k-1]
N = 2
K = 1
print(Solution().kthGrammar(N, K))