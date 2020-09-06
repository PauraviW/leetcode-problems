class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:

        pass
        # if grid:
        #     one_set = set()
        #     two_set = set()
        #
        #     # collect 1 and 2 data
        #     for i in range(len(grid)):
        #         for j in range(len(grid[0])):
        #             print(grid[i][j])
        #             if grid[i][j] == 1:
        #                 one_set.add((i, j))
        #             elif grid[i][j] == 2:
        #                 two_set.add((i, j))
        #
        #     print(len(two_set), len(one_set))
        #     if len(one_set) == 0:
        #         return 0
        #
        #     if len(two_set) == 0:
        #         return -1
        #     count = 0
        #     l = 0
        #     while l != len(one_set):
        #         count += 1
        #         l = len(one_set)
        #         temp = set()
        #         for i, j in two_set:
        #             print("coordinates", (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
        #             if (i - 1, j) in one_set:
        #                 temp.add((i - 1, j))
        #                 one_set.remove((i - 1, j))
        #             if (i + 1, j) in one_set:
        #                 temp.add((i + 1, j))
        #                 one_set.remove((i + 1, j))
        #             if (i, j - 1) in one_set:
        #                 temp.add((i, j - 1))
        #                 one_set.remove((i, j - 1))
        #             if (i, j + 1) in one_set:
        #                 temp.add((i, j + 1))
        #                 one_set.remove((i, j + 1))
        #         two_set = two_set | temp
        #     return count - 1 if len(one_set) == 0 else -1


grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid))