def solve_n_queens(n):
    def create_board(state):
        board = []
        for row in state:
            board.append('.' * row + 'Q' + '.' * (n - row - 1))
        return board

    def backtrack(row=0, diagonals=set(), anti_diagonals=set(), cols=set(), state=[]):
        if row == n:
            solutions.append(create_board(state))
            return
        for col in range(n):
            diag = row - col
            anti_diag = row + col
            if col in cols or diag in diagonals or anti_diag in anti_diagonals:
                continue
            cols.add(col)
            diagonals.add(diag)
            anti_diagonals.add(anti_diag)
            state.append(col)
            backtrack(row + 1, diagonals, anti_diagonals, cols, state)
            cols.remove(col)
            diagonals.remove(diag)
            anti_diagonals.remove(anti_diag)
            state.pop()

    solutions = []
    backtrack()
    return solutions

# Example usage:
n = 4
print(solve_n_queens(n))
