board = [' ' for i in range(9)]

def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

def check_win(player):
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    elif board[3] == player and board[4] == player and board[5] == player:
        return True
    elif board[6] == player and board[7] == player and board[8] == player:
        return True
    elif board[0] == player and board[3] == player and board[6] == player:
        return True
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    elif board[0] == player and board[4] == player and board[8] == player:
        return True
    elif board[2] == player and board[4] == player and board[6] == player:
        return True
    else:
        return False

def play_game():
    print_board()
    player = 'X'
    while True:
        print(f"It's {player}'s turn.")
        move = int(input('Enter position (1-9): '))
        if board[move - 1] == ' ':
            board[move - 1] = player
            print_board()
            if check_win(player):
                print(f'{player} wins!')
                break
            if ' ' not in board:
                print("It's a tie!")
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print('That position is already taken. Try again.')
    
play_game()