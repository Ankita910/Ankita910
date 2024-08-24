def solve_sudoku(board):
    if is_board_complete(board):
        return True

    row, col = find_empty_cell(board)

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def is_board_complete(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# Get Sudoku input from the user
board = []
print("Enter the Sudoku puzzle, row by row:")
for _ in range(9):
    row = list(map(int, input().split()))
    board.append(row)

solve_sudoku(board)

# Output the solved board
print("Solved Sudoku:")
for row in board:
    print(row)



