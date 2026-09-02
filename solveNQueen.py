def solveNQueen(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if solveNQUtil(board, 0, n):
        return board
    else:
        return None

def solveNQUtil(board, col, n):
    if col == n:
        return True
    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            if solveNQUtil(board, col + 1, n):
                return True
            board[i][col] = 0
    return False

def isSafe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

n = 4
board = solveNQueen(n)
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()
    
    