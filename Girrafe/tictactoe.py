# global variable
# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]
# If game is still going
game_still_going = True
# Who won or tie
winner = None

# Whose turn it is
current_player = "X"


# The display board


def display_board():
    print("{0}|{1}|{2}".format(board[0], board[1], board[2]))
    print("{0}|{1}|{2}".format(board[3], board[4], board[5]))
    print("{0}|{1}|{2}".format(board[6], board[7], board[8]))


# Play the game


def play_game():
    # display initial board
    display_board()
    # While the game is still going
    while game_still_going:
        # Handle a single turn of the player
        handle_turn(current_player)
        # Check it the game has ended
        check_if_game_over()
        # Flip to the other player
        flip_player()
    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner is None:
        print("Tie.")


# Handle a single turn of a player
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Chose a position from 1 - 9: ")
    valid = False
    while not valid:
        while position not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            position = input("Chose a position from 1 - 9: ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("You cant go in there. Go again")

    board[position] = player
    display_board()


# TO check if the game over
def check_if_game_over():
    check_if_win()
    check_if_tie()


# To check if there is winner
def check_if_win():
    # to set up global variable
    global winner
    # check rows
    row_winner = check_rows()
    # check column
    column_winner = check_column()
    # check diagonals
    diagonal_winner = check_diagonal()
    if row_winner:
        # there is a win
        winner = row_winner
    elif column_winner:
        # there is a win
        winner = column_winner
    elif diagonal_winner:
        # there is a win
        winner = diagonal_winner
    else:
        # there is no win
        winner = None
    return


def check_rows():
    # set up global variable
    global game_still_going
    # check if any of the row have the same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_3 or row_2:
        game_still_going = False
    # return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_column():
    # set up global variable
    global game_still_going
    # check if any of the column have the same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if any column does have a match than to stop
    if column_1 or column_3 or column_2:
        game_still_going = False
    # return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonal():
    # set up global variable
    global game_still_going
    # check if any of the diagonal have the same value
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # if any diagonal does have a match than to stop
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return


# TO check if it tie
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


# The flip player
def flip_player():
    # Global variable
    global current_player
    # IF the current player is X then change to O
    if current_player == "X":
        current_player = "O"
    # If current player is O then change to X
    elif current_player == "O":
        current_player = "X"
    return


play_game()

# board
# display board
# play game
# handle turn
# check win
# check rows
# check column
# check diagonals
# check tie
# flip player
