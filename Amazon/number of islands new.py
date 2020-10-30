island = [[1,1,1,1,0],[0,0,0,1,1],[0,0,0,0,0],[1,1,0,1,1]]
island = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
count = 0

visited = set()
def isValid(i,j):
    if i >=0 and j >=0 and i < len(island) and j < len(island[0]) and island[i][j] == "1":

        return True
candidates = [(0,1), (1,0), (0,-1), (-1,0)]
def dfs(i,j):

    if i < 0 or j < 0 or i >= len(island) or j >= len(island[0]):
        return
    for x, y in candidates:
        if isValid(i+x, j+y) and (i+x, j+y) not in visited:
            visited.add((i + x, j + y))
            dfs(i+x, j+y)


for i in range(len(island)):
    for j in range(len(island)):
        if island[i][j] == "1" and (i,j) not in visited:
            visited.add((i, j))
            dfs(i, j)
            count += 1
print(count)