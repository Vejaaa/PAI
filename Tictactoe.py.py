def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board, player):
    return any(all(cell == player for cell in row) for row in board) or \
           any(all(board[row][col] == player for row in range(3)) for col in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))
def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)
def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = players[0]
    while True:
        print_board(board)
        row, col = map(int, input(f"Player {current_player}, enter row and column (0, 1, or 2) separated by space: ").split())
        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Cell already taken. Try again.")
            continue
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        current_player = players[1] if current_player == players[0] else players[0]
tic_tac_toe()