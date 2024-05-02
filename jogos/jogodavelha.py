# Tic Tac Toe game in Python

# Function to print the Tic Tac Toe board
def print_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('-----------')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('-----------')
    print(f' {board[6]} | {board[7]} | {board[8]} ')

# Function to check if a player has won the game
def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (i.e., the game is a tie)
def check_full(board):
    return ' ' not in board

# Function to get a player's move
def get_move(player):
    valid_move = False
    while not valid_move:
        move = input(f'Player {player}, enter your move (1-9): ')
        if move.isdigit() and int(move) in range(1, 10) and board[int(move) - 1] == ' ':
            board[int(move) - 1] = player
            valid_move = True
        else:
            print('Invalid move. Try again.')

# Main game loop
board = [' '] * 9
current_player = 'X'

while True:
    print_board(board)
    if check_win(board, current_player):
        print_board(board)
        print(f'Player {current_player} wins!')
        break
    elif check_full(board):
        print_board(board)
        print('It\'s a tie!')
        break
    else:
        get_move(current_player)
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'