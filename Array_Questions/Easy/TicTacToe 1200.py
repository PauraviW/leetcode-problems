class Solution:
    def tictactoe(self, moves: [[int]]) -> str:
        A_moves = [moves[i] for i in range(0, len(moves), 2)]
        B_moves = [moves[i] for i in range(1, len(moves), 2)]

        # A horizontal vertical

# moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
print(Solution().tictactoe(moves))