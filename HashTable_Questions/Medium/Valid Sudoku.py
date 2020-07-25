from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        diagonals = defaultdict(set)

        for i in range(len(board)):
            l1 = set()
            l = set()
            for j in range(len(board[0])):
                if board[i][j].isdigit():
                    if board[i][j] not in l1:
                        l1.add(board[i][j])
                    else:
                        return False
                    if board[i][j] in diagonals[(i//3)*3 + j//3]:
                        return False
                    else:
                        diagonals[(i//3)*3 + j//3].add(board[i][j])
                if board[j][i].isdigit():
                    if board[j][i] not in l:
                        l.add(board[j][i])
                    else:
                        return False

        return True

input = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
# input = [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
print(Solution().isValidSudoku(input))