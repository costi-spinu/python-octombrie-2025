# Task 3
# There are an 8×8 chessboard and a knight. The program should request
# the coordinates of the square from the user and put the knight there.
# The program's objective is to find the knight's path that allows it
# to go through the entire chessboard while stepping on each square only
#  once. (Since the process of finding a path for initial squares
# can take a long time, we recommend you to begin with a 6×6 chessboard).
#  Use recursion in your game.


N = 8  # board size (can be 8 for full chessboard)

# All 8 possible knight moves
moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]


def is_valid(x, y, board):
    """Check if (x, y) is a valid move."""
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1


def print_board(board):
    """Print the board with knight's path."""
    for row in board:
        print(" ".join(f"{c:2}" for c in row))
    print()


def solve_knight(x, y, move_count, board):
    """Recursive function to solve Knight's Tour."""
    if move_count == N * N:  # all squares visited
        return True

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, board):
            board[nx][ny] = move_count
            if solve_knight(nx, ny, move_count + 1, board):
                return True
            board[nx][ny] = -1  # backtrack

    return False


def knight_tour(start_x, start_y):
    """Driver function for Knight’s Tour."""
    board = [[-1 for _ in range(N)] for _ in range(N)]
    board[start_x][start_y] = 0  # starting square

    if not solve_knight(start_x, start_y, 1, board):
        print("❌ No solution found.")
    else:
        print("✅ Knight’s Tour solution:")
        print_board(board)


# ---- Run program ----
if __name__ == "__main__":
    print(f"♞ Knight’s Tour on {N}x{N} board")
    sx = int(input("Enter starting row (0-indexed): "))
    sy = int(input("Enter starting column (0-indexed): "))
    knight_tour(sx, sy)
