class Solution:
    def shiftGrid(self, grid: [[int]], k: int) -> [[int]]:
        l = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                l.append(grid[i][j])
        shift = k % (len(grid[0])*len(grid))

        new_array = l[-shift:] + l[0:len(l) - shift]
        print(new_array)
        v = []
        for i in range(len(grid)):
            b = []
            for j in range(len(grid[0])):
                b.append(new_array.pop(0))
            v.append(b)
        print(v)

grid = [
           [1,2,3],
           [4,5,6],
           [7,8,9]]
k = 1
print(Solution().shiftGrid(grid, k))