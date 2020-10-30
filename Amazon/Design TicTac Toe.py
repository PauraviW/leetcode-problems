class TicTacToe:
    def __init__(self, m):
        self.rows = [0]*m
        self.cols = [0]*m
        self.diag1 = 0
        self.diag2 = 0
        self.m = m

    def move(self,player, row, col):
        self.rows[row] += 1 if player == 1 else -1
        self.cols[col] += 1 if player == 1 else - 1
        if row == col:
            self.diag1 += 1 if player == 1 else - 1
        if row + col == self.m:
            self.diag2 += 1 if player == 1 else -1
        if abs(self.rows[row]) == self.n or abs(self.cols[col] == self.n) or abs(self.diag2) == self.n or abs(self.diag1) == self.n:
            return 1 if player == 1 else 2
        return 0

