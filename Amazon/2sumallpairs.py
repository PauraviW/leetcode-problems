l = [2,9,11,0,6]

target = 11
ans = []
visited = {}
for i in range(len(l)):
    if target - l[i] in visited:
       ans.append((visited[target-l[i]], i))
    visited[l[i]] = i
print(ans)