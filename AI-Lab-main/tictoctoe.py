import random

def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)

def check_winner(board, player):
    for i in range(0, 9, 3):
        if all(cell == player for cell in board[i:i+3]):
            return True

    for col in range(3):
        if all(board[row*3+col] == player for row in range(3)):
            return True

    if all(board[i] == player for i in [0, 4, 8]) or all(board[i] == player for i in [2, 4, 6]):
        return True

    return False

def is_full(board):
    return all(cell != " " for cell in board)

def computer_move(board):
    available_moves = [i+1 for i in range(9) if board[i] == " "]
    return random.choice(available_moves)

def main():
    board = [" " for _ in range(9)]
    user_symbol = "X"
    computer_symbol = "O"
    current_player = user_symbol

    while True:
        print_board(board)

        if current_player == user_symbol:
            while True:
                    move = int(input("Enter a number (1-9) to make your move: "))
                    if 1 <= move <= 9 and board[move - 1] == " ":
                        break
                    else:
                        print("Invalid move. Try again.")
            board[move - 1] = current_player
        else:
            print("Computer's turn:")
            move = computer_move(board)
            board[move - 1] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = user_symbol if current_player == computer_symbol else computer_symbol
main()