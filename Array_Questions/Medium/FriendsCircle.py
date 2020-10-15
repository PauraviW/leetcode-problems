from collections import defaultdict, deque

M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
# M = [[1,1,0],[1,1,0],[0,0,1]]
M = [[1,0,0],[0,1,0],[0,0,1]]
dic = defaultdict(set)

for i in range(len(M)):
    for j in range(len(M)):
        if M[i][j] == 1:
            dic[i].add(j)
friends = [i for i in range(0, len(M))]
queue = deque([0])
visited = set()
visited.add(0)
ans = 0
while friends:
    curr1 = friends[0]
    queue.append(curr1)
    while queue:
        curr = queue.popleft()
        for i in dic[curr]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
                friends.remove(i)
    else:
        ans += 1
    if friends:
        friends.remove(curr1)
print(ans)


