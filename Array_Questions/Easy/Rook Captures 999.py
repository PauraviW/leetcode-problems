class Solution:
    def numRookCaptures(self, board: [[str]]) -> int:

        # move in all 4 directions till it meets an obstacle
        l = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    rook_position = (i,j)
                    break
        for i in range(rook_position[0], 8):
            if board[i][rook_position[1]] == 'p' or board[i][rook_position[1]] == 'B':
                l.append((i,rook_position[1], board[i][rook_position[1]]))
                break

        for i in reversed(range(0, rook_position[0])):
            if board[i][rook_position[1]] == 'p' or board[i][rook_position[1]] == 'B':
                l.append((i,rook_position[1], board[i][rook_position[1]]))
                break

        for i in reversed(range(0, rook_position[1])):
            if board[rook_position[0]][i] == 'p' or board[rook_position[0]][i] == 'B':
                l.append((rook_position[0],i, board[rook_position[0]][i]))
                break

        for i in range(rook_position[1], 8):
            if board[rook_position[0]][i] == 'p' or board[rook_position[0]][i] == 'B':
                l.append((rook_position[0], i, board[rook_position[0]][i]))
                break
        print(l)
        count = 0
        for i,j,letter in l:
            if letter == 'p':
                count+=1
        return count

board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
print(Solution().numRookCaptures(board))