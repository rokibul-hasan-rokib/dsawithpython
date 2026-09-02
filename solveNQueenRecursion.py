def solveNQueen(n):
    solutions = []
    board = [-1] * n;
    
    def isSafe(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True
    
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if isSafe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
                
    backtrack(0)
    return solutions

print(len(solveNQueen(8)))  # Output: 92