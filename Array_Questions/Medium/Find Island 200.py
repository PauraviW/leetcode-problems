class Solution:





    def numIslands(self, grid: [[str]]) -> int:
        zero_st = [(0, 0)]
        one_st = []
        visited = set()
        # visited.add((0,0))
        def add_in_set(i, j):
            if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]):
                flag = False
                if (i, j) not in visited:
                    if grid[i][j] == '1':
                        one_st.append((i, j))
                        flag = True
                    else:
                        zero_st.append((i, j))
                        flag = False
                    visited.add((i, j))
                    return flag
            return False
        if grid:
            ans = 0
            while zero_st:
                i, j = zero_st.pop(0)
                flag = add_in_set(i-1, j) or  add_in_set(i, j - 1) or add_in_set(i+1, j) or add_in_set(i, j + 1) or add_in_set(i, j)
                if flag:
                    ans += 1
                    while one_st:
                        k, l = one_st.pop(0)
                        add_in_set(k - 1, l)
                        add_in_set(k, l - 1)
                        add_in_set(k + 1, l)
                        add_in_set(k, l + 1)
        return ans




grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
grid = [
  ["1","1","1","1","1"],
  ["1","1","1","1","1"],
  ["1","1","0","1","1"],
  ["1","1","1","1","1"]
]
grid = [
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"]
]
# grid = [["0", "0"]]
print(Solution().numIslands(grid))
