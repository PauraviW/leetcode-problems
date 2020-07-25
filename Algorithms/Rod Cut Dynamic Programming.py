

def rod_cut(p, n):
    if n == 0:
        return 0
    q = -float("inf")
    for  i in range(1, n+1):
        q = max(q, p[i] + rod_cut(p, n-i))
    return q






p = [1, 5, 8, 9, 10, 17,  20, 24, 30]
n = 4
print(rod_cut(p, n))