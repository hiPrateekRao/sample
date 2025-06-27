def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!\nPlayer 1 is X, Player 2 is O")

    while True:
        print_board(board)
        try:
            move = input(f"Player {current_player}, enter your move (row and column, 1-3 each, space-separated): ")
            row, col = map(int, move.strip().split())
            row -= 1
            col -= 1
        except ValueError:
            print("Invalid input. Please enter two numbers between 1 and 3 separated by space.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid move. Position out of range.")
            continue
        if board[row][col] != " ":
            print("That position is already taken. Choose another.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
