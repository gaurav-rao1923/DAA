1 
 
def is_safe(board, row, col, N):
 2 
 
    # Check if it is safe to place a queen at position (row, col)
 3 
 
    # Check for the same column
 4 
 
    for i in range(row):
 5 
 
        if board[i][col] == "Q":
 6 
 
            return False
 7 
 
    # Check for the upper left diagonal
 8 
 
    i = row - 1
 9 
 
    j = col - 1
 10 
 
    while i >= 0 and j >= 0:
 11 
 
        if board[i][j] == "Q":
 12 
 
            return False
 13 
 
        i -= 1
 14 
 
        j -= 1
 15 
 
    # Check for the upper right diagonal
 16 
 
    i = row - 1
 17 
 
    j = col + 1
 18 
 
    while i >= 0 and j < N:
 19 
 
        if board[i][j] == "Q":
 20 
 
            return False
 21 
 
        i -= 1
 22 
 
        j += 1
 23 
 
    return True
 24 
 
 25 
 
def solve_n_queens(board, row, N, solutions):
 26 
 
    # Base case: All queens have been placed
 27 
 
    if row == N:
 28 
 
        solutions.append([''.join(row) for row in board])
 29 
 
        return
 30 
 
    for col in range(N):
 31 
 
        if is_safe(board, row, col, N):
 32 
 
            board[row][col] = "Q"
 33 
 
            solve_n_queens(board, row + 1, N, solutions)
 34 
 
            board[row][col] = "."
 35 
 
 36 
 
def n_queens_solver(N):
 37 
 
    board = [["." for _ in range(N)] for _ in range(N)]
 38 
 
    solutions = []
 39 
 
    solve_n_queens(board, 0, N, solutions)
 40 
 
    return solutions
 41 
 
 42 
 
def main():
 43 
 
    # Example usage
 44 
 
    N = 4
 45 
 
    solutions = n_queens_solver(N)
 46 
 
    if len(solutions) == 0:
 47 
 
        print("Not possible")
 48 
 
    else:
 49 
 
        for solution in solutions:
 50 
 
            for row in solution:
 51 
 
                print(row)
 52 
 
            print()
 53 
 
 54 
 
if __name__ == "__main__":
 55 
 
    main()
