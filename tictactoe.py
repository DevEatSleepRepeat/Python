import random

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

def ai_move(board, ai_symbol, human_symbol):
    # Implement AI logic here
    # For simplicity, the AI makes a random move
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    if available_moves:
        row, col = random.choice(available_moves)
        board[row][col] = ai_symbol

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human_symbol = 'X'
    ai_symbol = 'O'

    print("Welcome to Tic Tac Toe!")
    while True:
        print_board(board)
        if is_full(board):
            print("It's a draw!")
            break

        # Human player's turn
        try:
            row, col = map(int, input(f"Your move (row column): ").split())
            if board[row][col] != ' ':
                raise ValueError
            board[row][col] = human_symbol
        except (ValueError, IndexError):
            print("Invalid move. Try again.")
            continue

        if check_winner(board, human_symbol):
            print_board(board)
            print("You win!")
            break

        # AI's turn
        ai_move(board, ai_symbol, human_symbol)

if __name__ == "__main__":
    play_game()