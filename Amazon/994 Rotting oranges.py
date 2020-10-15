class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:

        rotten = []
        fresh = []

        # rotten and fresh count
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh.append((i, j))
        visited = set()

        def check(i, j):
            if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])and grid[i][j] == 1:
                    return True

        mins = 0
        flag = True
        temp = []
        adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # while True:
        #     while rotten:
        #         i, j = rotten.pop()
        #         visited.add((i, j))
        #         for k, l in adj:
        #             if (i + k, j + l) not in visited and check(i + k, j + l):
        #                 temp.append((i + k, j + l))
        #             visited.add((i + k, j + l))
        #     if not rotten and temp:
        #         rotten, temp = temp, rotten
        #         mins += 1
        #     elif not rotten and not temp:
        #         break
        while rotten or temp:
            i, j = rotten.pop()
            visited.add((i, j))
            for k, l in adj:
                if (i + k, j + l) not in visited and check(i + k, j + l):
                    temp.append((i + k, j + l))
                visited.add((i + k, j + l))
            if not rotten and temp:
                rotten, temp = temp, rotten
                mins += 1

        print(mins)



grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid))