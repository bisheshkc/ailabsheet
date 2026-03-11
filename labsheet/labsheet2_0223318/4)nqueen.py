def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()


def is_safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueen(board, row, n):

    if row == n:
        print_solution(board, n)
        return True

    for col in range(n):

        if is_safe(board, row, col, n):
            board[row][col] = 1

            solve_nqueen(board, row + 1, n)

            board[row][col] = 0   # Backtrack

    return False


# Main program
n = int(input("Enter number of queens: "))
board = [[0 for _ in range(n)] for _ in range(n)]

solve_nqueen(board, 0, n)