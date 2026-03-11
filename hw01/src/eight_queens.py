class EightQueens:
    def __init__(self, n=8):
        self.n = n
        self.solutions = []

    def is_safe(self, board, row, col):
        for i in range(row):
            if board[i] == col:
                return False
            if abs(row - i) == abs(col - board[i]):
                return False
        return True

    def backtrack(self, board, row):
        if row == self.n:
            self.solutions.append(board.copy())
            return
        for col in range(self.n):
            if self.is_safe(board, row, col):
                board[row] = col
                self.backtrack(board, row + 1)
                board[row] = -1

    def solve(self):
        self.solutions = []
        self.backtrack([-1] * self.n, 0)
        return self.solutions

if __name__ == "__main__":
    solver = EightQueens(8)
    print(f"8皇后解数：{len(solver.solve())}")
