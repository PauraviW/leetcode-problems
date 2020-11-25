class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        if not grid:
            return 0
        self.visited = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in self.visited:
                    if grid[i][j] == '1':
                        self.dfs(grid, i, j)
                        count += 1
        return count
    def dfs(self, grid, i ,j):
        if (i, j) not in self.visited:
            if i>=0 and j >= 0 and i < len(grid) and j < len(grid[0]) and grid[i][j] == '1':
                self.visited.add((i,j))
                self.dfs(grid, i-1, j)
                self.dfs(grid, i + 1, j)
                self.dfs(grid, i , j - 1)
                self.dfs(grid, i, j + 1)

grid = [  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]
print(Solution().numIslands(grid))