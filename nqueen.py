def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False  
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True
def solve_n_queens_util(board, row, n, solutions):
    if row == n:     
        solutions.append(["".join([" Q " if cell == 1 else " - " for cell in row]) for row in board])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row][col] = 0  # Backtrack
def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

def print_solutions(solutions):
    print(f"Total solutions = {len(solutions)}\n")
    for idx, solution in enumerate(solutions):
        print(f"Solution {idx + 1}:")
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    N = int(input("Enter Number of Queens : "))  # Change N to the desired board size.
    solutions = solve_n_queens(N)
    if solutions:
        print_solutions(solutions)
    else:
        print(f"No solutions found for N = {N}.")