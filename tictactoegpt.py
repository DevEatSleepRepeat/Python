import random

# Function to display the board
def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check if someone has won
def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[pos] == player for pos in condition) for condition in win_conditions)

# Function to check if the board is full
def is_full(board):
    return all(space != " " for space in board)

# Function for the AI to make a move
def ai_move(board):
    # Try to win or block opponent's win
    for player in ["O", "X"]:  
        for i in range(9):
            if board[i] == " ":
                board[i] = player
                if check_win(board, player):
                    board[i] = "O"  # AI claims the spot
                    return
                board[i] = " "  # Undo move

    # If no immediate win/block, pick a random empty spot
    empty_spots = [i for i in range(9) if board[i] == " "]
    board[random.choice(empty_spots)] = "O"

# Main game function
def play_game():
    board = [" "] * 9
    print("Welcome to Tic Tac Toe! You are X and the AI is O.")
    display_board(board)

    while True:
        # Player's turn
        try:
            move = int(input("Choose your move (1-9): ")) - 1
            if board[move] != " " or move not in range(9):
                print("Invalid move. Try again.")
                continue
        except (ValueError, IndexError):
            print("Please enter a number between 1 and 9.")
            continue

        board[move] = "X"
        display_board(board)

        if check_win(board, "X"):
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        # AI's turn
        print("AI is making its move...")
        ai_move(board)
        display_board(board)

        if check_win(board, "O"):
            print("The AI wins! Better luck next time!")
            break
        if is_full(board):
            print("It's a tie!")
            break

# Start the game
if __name__ == "__main__":
    play_game()x