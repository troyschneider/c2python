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

#def display_game(game):
    #You will need to draw the game board with the new move
    #You will have to use the game variable that was passed in
    #Try looking at start_game above for an idea

#def get_move(request):
    #use input to read in a number
    #check to make sure that the selected move is valid (not a letter)
    #you are going to have to convert things (input takes in a string, you will need to convert it)
    #check for things like the range (What happens if you enter 100000? What if you type in a letter instead?)
    #make sure to save it to a variable and return it

#def check_move(rowIn, colIn, game):
    #make sure to check that you are playing in a open space
    #return either True if the move is valid, or False if the move is illegal

#def add_move(rowIn, colIn, game, symbol):
    #insert the new move into the game board
    #notice that we have passed the symbol (X or O) so we don't care whose turn it is
    #return game

#def check_for_winner(game):
    #You will have to check every configuration (rows, columns, and diagonals) for winners
    #There are many ways to do this
    #Return True if there is a winner, and False if there is not


if __name__ == '__main__':
    #This works, but what if you want to play more?
    #Try adding a loop that asks the players if they want to try again
    #Once you can play again, try adding a scoreboard that lets you know how many game each player has won

    game = start_game()
    player = 2
    winner = False
    symbol = ''
    turn = 0

    # go on forever
    while winner == False and turn < 9:
        if player == 1:
            player = 2
        else:
            player = 1
        print("Turn: Player " + str(player))
        goodMove = False
#        while not goodMove:
#            rowIn = get_move("Play in which row? (Starts at 1)")
#            colIn = get_move("Play in which column? (Starts at 1)")
#            goodMove = check_move(rowIn, colIn, game)
        if player == 1:
            symbol = "X"
        else:
            symbol = "O"
#        game = add_move(rowIn, colIn, game, symbol)
#        display_game(game)
#        winner = check_for_winner(game)
        turn = turn + 1
    if winner == False:
        print("The game has ended in a tie.")
    else:
        print("Player " + str(player) + " wins!")
