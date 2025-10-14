# Task 4
# Develop a game of 15 Puzzle.
import random

SIZE = 4  # 4x4 board


def create_board():
    """Create a shuffled 15-puzzle board (4x4)."""
    nums = list(range(1, SIZE * SIZE))
    nums.append(0)  # 0 represents the empty space
    random.shuffle(nums)
    board = [nums[i * SIZE : (i + 1) * SIZE] for i in range(SIZE)]
    return board


def print_board(board):
    """Print the board in a user-friendly way."""
    for row in board:
        print(" ".join(f"{n:2}" if n != 0 else " _" for n in row))
    print()


def find_empty(board):
    """Find the (row, col) of the empty space (0)."""
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 0:
                return r, c


def is_solved(board):
    """Check if the board is solved."""
    nums = [board[r][c] for r in range(SIZE) for c in range(SIZE)]
    return nums == list(range(1, SIZE * SIZE)) + [0]


def move(board, direction):
    """Move the empty space in the given direction if possible."""
    r, c = find_empty(board)
    if direction == "w" and r < SIZE - 1:  # Move up
        board[r][c], board[r + 1][c] = board[r + 1][c], board[r][c]
    elif direction == "s" and r > 0:  # Move down
        board[r][c], board[r - 1][c] = board[r - 1][c], board[r][c]
    elif direction == "a" and c < SIZE - 1:  # Move left
        board[r][c], board[r][c + 1] = board[r][c + 1], board[r][c]
    elif direction == "d" and c > 0:  # Move right
        board[r][c], board[r][c - 1] = board[r][c - 1], board[r][c]
    else:
        print("❌ Invalid move!")


def play(board, moves=0):
    """Recursive game loop."""
    print_board(board)
    if is_solved(board):
        print(f"🎉 Congratulations! You solved the puzzle in {moves} moves.")
        return

    move_dir = input("Move (w=up, s=down, a=left, d=right): ").lower()
    move(board, move_dir)
    play(board, moves + 1)


# Start the game
if __name__ == "__main__":
    print("🧩 Welcome to the 15 Puzzle Game!")
    board = create_board()
    play(board)
