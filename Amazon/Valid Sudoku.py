def validSudoku(grid):
    for i in range(len(grid)):
        if len(set(grid[i])) != len(grid[i]):
            return False
    for i in zip(*grid):
        if len(set(i))  != len(i):
            return False

    for i in (0,3,6):
        for j in range(0, 3, 6):
            temp = []
            for k in range(i, i+3):
                for l in range(j, j+3):
                    temp.append(grid[k][l])
            print(temp)
            if len(temp) != len(set(temp)):
                return False
    return True


[[".",".",".",".","5",".",".","1","."],
 [".","4",".","3",".",".",".",".","."],
 [".",".",".",".",".","3",".",".","1"],
 ["8",".",".",".",".",".",".","2","."],
 [".",".","2",".","7",".",".",".","."],
 [".","1","5",".",".",".",".",".","."],
 [".",".",".",".",".","2",".",".","."],
 [".","2",".","9",".",".",".",".","."],
 [".",".","4",".",".",".",".",".","."]]