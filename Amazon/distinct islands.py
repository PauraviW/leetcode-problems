class Solution:

    def dfs(self, i, j ,nodes, grid, visited):
        if i < len(grid) and j < len(grid[0]) and i >=0 and j >=0 and grid[i][j] == 1 and (i,j) not in visited:
            nodes.append([i,j])
            visited.add((i,j))
            for k ,v in [(0,1), (1,0), (0,-1), (-1, 0)]:
                nodes = self.dfs(i+k,v+j, nodes, grid, visited)
        return nodes

    def distinctIslands(self, grid):

        visited = set()
        ans = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    nodes = self.dfs(i,j, [], grid, visited)
                    temp = set()
                    for x, y in nodes:
                        x -= i
                        y -= j
                        temp.add((x,y))
                    ans.add(tuple((x,y)))
                    print(nodes)
        return len(ans)
print(Solution().distinctIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))