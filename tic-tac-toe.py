player_1 = ''
while player_1 != 'x' and player_1 != 'o':
    player_1 = input('Player 1 would you like to be X or O').lower()
    if player_1 == 'x':
        player_2 = 'o'
    elif player_1 == 'o':
        player_2 = 'x'
    else:
        print('Please choose a valid team')
placement = list(range(1,10))
def print_board():
    print(f'     |     |     \n  {placement[0]}  |  {placement[1]}  |  {placement[2]}   \n     |     |     \n-----------------\n     |     |     \n  {placement[3]}  |  {placement[4]}  |  {placement[5]}   \n     |     |     \n-----------------\n     |     |     \n  {placement[6]}  |  {placement[7]}  |  {placement[8]}   \n     |     |     \n' )
moves = 0
current_player = 1
print_board()
placement = [' ']*9
possible_wins=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
def check_win(made_moves, player):
    for wins in possible_wins:
        spots=[]
        for positions in wins:
            spots.append(made_moves[positions-1])
            if spots == [player]*3:
                return True
while moves < 9:
    def replay():
        replay = input('Would you like to replay(y/n)').lower()
        return replay == 'y'
    current_move = int(input(f'Player {current_player} where would you like to play [1-9]'))
    if placement[current_move-1] == ' ':
        if current_player == 1:
            placement[current_move-1] = player_1
            moves += 1
            print_board()
            if check_win(placement,player_1):
                print(f'Player {current_player} has won')
                if replay():
                    moves = 0
                    placement = [' ']*9
                    print_board()
                else:
                    print('Good Game')
                    break
            current_player = 2
        else:
            placement[current_move-1] = player_2
            moves += 1
            print_board()
            if check_win(placement,player_2):
                print(f'Player {current_player} has won')
                if replay():
                    moves = 0
                    placement = [' ']*9
                    print_board()
                else:
                    print('Good Game')
                    break
            current_player = 1
    else:
        print(f'Spot {current_move} already chosen, please choose a valid spot')
    if moves == 9:
        if replay():
            moves = 0
            placement = [' ']*9
            print_board()
        else:
            print('Good Game')
            break
