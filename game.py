# Function to display the Tic-Tac-Toe board
def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


# Function to check if a player has won
def check_winner(board, player):
    # Check all possible winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


# Function to check if the board is full (tie)
def check_tie(board):
    return all(cell != " " for cell in board)


# Main game function
def tic_tac_toe():
    # Initialize the board
    board = [" " for _ in range(9)]
    current_player = "X"  # X starts first

    print("Welcome to Tic-Tac-Toe!")
    display_board(board)

    while True:
        # Get the player's move
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move! Please enter a number between 1 and 9.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # Check if the selected cell is empty
        if board[move] == " ":
            board[move] = current_player
            display_board(board)

            # Check if the current player has won
            if check_winner(board, current_player):
                print(f"Player {current_player} wins! 🎉")
                break

            # Check if the game is a tie
            if check_tie(board):
                print("It's a tie! 🤝")
                break

            # Switch players
            current_player = "O" if current_player == "X" else "X"
        else:
            print("That cell is already taken! Try again.")


# Run the game
if __name__ == "__main__":
    tic_tac_toe()