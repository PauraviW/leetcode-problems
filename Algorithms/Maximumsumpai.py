from collections import defaultdict
arr = []
def f(arr):
    map = defaultdict(list)

    for x in arr:
        ds = 0
        n = x
        while n > 0:
            ds += n%10
            n = n//10

        map[ds].append(x)

    ans = -1
    
    for k, v in map.items():
        map[k] = sorted(v, reverse=True)
        if len(v) >=2:
            ans = max(ans, map[k][0]+ map[k][1])
    return ans

print(f([51,71,17,42]))