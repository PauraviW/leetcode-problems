class Solution:
    def divisorGame(self, N: int) -> bool:
        count = 0

        while N != 1:

            max_val = 0
            for i in range(1, int(N / 2)+1):
                print("i", i)
                if N % i == 0:
                    if max_val < i:
                        max_val = i
            print("Max", max_val, N)
            N = N - max_val

            count += 1

        print(count)
N = 13
print(Solution().divisorGame(N))



def aa(chars, words):
    d = {x: chars.count(x) for x in set(chars)}
    cnt = 0
    for w in words:
        for c in w:
            if c not in d:
                break
            if w.count(c) > d[c]:
                break
        else:
            cnt += len(w)
    return cnt