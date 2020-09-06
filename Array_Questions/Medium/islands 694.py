class Solution:
    def numDistinctIslands(self, grid: [[int]]) -> int:

        def islands(x, y, zero_stack, one_stack):
            if grid[x][y] == 1:
                one_stack.append((x,y))
            else:
                zero_stack.append((x,y))
            islands(x + 1, y, zero_stack, one_stack)
            islands(x - 1, y, zero_stack, one_stack)
            islands(x, y + 1, zero_stack, one_stack)
            islands(x , y - 1, zero_stack, one_stack)
            return zero_stack, one_stack

        seen = set()
        zero_stack = [[0,0]]
        one_stack = []
        while zero_stack:
            x, y = zero_stack.pop()
            seen.add((x, y))













grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(Solution().numDistinctIslands(grid))