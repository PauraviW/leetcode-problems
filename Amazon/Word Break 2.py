class Solution:
    def isValid(self, k, v, board):
        if k >= 0 and v >= 0 and k < len(board) and v < len(board[0]):
            return True

    def findWords(self, board: [[str]], words: [str]) -> [str]:

        self.candidates = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(index, word, x, y, s):

            if index == len(word) and s== word:
                return True
            ans = False
            for i, j in self.candidates:
                if self.isValid(x + i, y + j, board) and (board[x + i][y + j] == word[index] or index == 0):
                    # if index == 0 or :
                    letter = board[x + i][y + j]
                    board[x + i][y + j] = '#'
                    ans = ans or dfs(index + 1, word, x + i, y + j, s+letter)
                    board[x + i][y + j] = word[index]
            return ans

        res = []
        for word in words:
            ans = dfs(0, word, -1, 0, '')
            if ans:
                res.append(word)
        return res

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
board = [["a"]]
words = ["b"]
print(Solution().findWords(board, words))
