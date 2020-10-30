class Solution:
    def exist(self, board: [[str]], word: str) -> bool:

        def isValid(x, y):
            if x < len(board) and y < len(board[0]) and x >= 0 and y >= 0:
                return True

        def bfs(i, j, curr, index):
            if curr == word:
                return True
            if index >= len(word):
                return False
            ans = False
            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if isValid(i + x, j + y) and board[i + x][j + y] == word[index]:
                    board[i + x][j + y] = '#'
                    ans = ans or bfs(i + x, j + y, curr + word[index], index + 1)
                    board[i + x][j + y] = word[index]
            return ans

        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == word[0]:
                    board[i][j] = '#'
                    ans = bfs(i, j, word[0], 1)
                    board[i][j] = word[0]
                    if ans:
                        return True
        return False
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
board = [["a","a"]]
word = "aaa"
print(Solution().exist(board, word))