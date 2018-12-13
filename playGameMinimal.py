def draw_line(row):
    rowout = "|"
    for entry in row:
        if entry == 0:
            entry = '_'
        rowout = rowout + str(entry) + "|"
    print(rowout)

def start_game():
    print(" _ _ _ ")
    for row_num in range(3):
        row = ["_","_","_"]
        draw_line(row)
    return [[0, 0, 0] for x in range(3)]

def display_game(game):
    print(" _ _ _ ")
    for row in game:
        draw_line(row)

def get_move(request):
    spot = input(request)
    return int(spot)


if __name__ == '__main__':
    keepPlaying = 'Y'
    player1Wins = 0
    player2Wins = 0


    game = start_game()
    player = 2
    winner = False
    turn = 0
    symbol = ''
    # go on forever
    while winner == False and turn < 9:
        if player == 1:
            player = 2
        else:
            player = 1
        print("Turn: Player {}".format(player))
        rowIn = get_move("Play in which row? (Starts at 0) ")
        colIn = get_move("Play in which column? (Starts at 0) ")
        if player == 1:
            symbol = "X"
        else:
            symbol = "O"
        game[rowIn][colIn] = symbol
        display_game(game)
        turn = turn + 1
