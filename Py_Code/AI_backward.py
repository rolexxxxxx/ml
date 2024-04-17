import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, alpha, beta, maximizing_player):
    if is_winner(board, 'X'):
        return -1
    elif is_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def make_optimal_move(board):
    best_val = float('-inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')
    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        move_val = minimax(board, 0, alpha, beta, False)
        board[i][j] = ' '
        if move_val > best_val:
            best_val = move_val
            best_move = (i, j)
        alpha = max(alpha, move_val)
    return best_move

def get_user_input():
    while True:
        try:
            x_value = int(input('Enter row (0, 1, or 2): '))
            y_value = int(input('Enter column (0, 1, or 2): '))
            if 0 <= x_value <= 2 and 0 <= y_value <= 2:
                return x_value, y_value
            else:
                print("Invalid input. Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

board = [[' ' for _ in range(3)] for _ in range(3)]
print_board(board)

while True:
    x_value, y_value = get_user_input()
    if  board[x_value][y_value] == ' ':
        board[x_value][y_value] = 'X'
    else:
        print('Invalid Input')
        continue

    print_board(board)

    if is_winner(board, 'X'):
        print('You win!')
        break

    if is_board_full(board):
        print('It\'s a draw!')
        break

    optimal_move = make_optimal_move(board)
    board[optimal_move[0]][optimal_move[1]] = 'O'
    print("AI's move:")

    print_board(board)

    if is_winner(board, 'O'):
        print('AI wins!')
        break
    if is_board_full(board):
        print('It\'s a draw!')
        break
