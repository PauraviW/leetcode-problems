def isValid(i,j):
    if i < len(grid) and j < len(grid[0]) and i >= 0 and j >= 0 and grid[i][j] == "1":
        return True
def dfs(i, j):


        for k, v in candidates:
            if isValid(i+k, j+v) and (i+k, j+v) not in visited:
                visited.add((i+k, j+v))
                dfs(i+k, j+v)

visited = set()
candidates = [(0,-1), (-1,0), (1,0), (0,1)]
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
grid = [["1","1","0","0","0"],  ["1","1","0","0","0"],  ["0","0","1","0","0"],  ["0","0","0","1","1"]
]
count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '1' and (i,j) not in visited:
            visited.add((i,j))
            dfs(i,j)
            count += 1
print(count)