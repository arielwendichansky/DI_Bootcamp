welcome_message = print("Welcome to TIC TAC TOE!")

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def display_board(board):
    print("*" * 11)
    for i,row in enumerate(board):
        print("*"+" | " .join(row) + "*")
        if i < len(board) -1:
            print("*"+"-"*2+"|"+"-"*3+"|"+"-"*2+"*")
    print("*" * 11)




def player_input():
    count_turns = 0
    winner = 0
    while count_turns < 10:
        display_board(board)
        if count_turns % 2 == 0:
            print('Player X is your turn')
            turn_symbol = "X"
            count_turns += 1
        else:
            print('Player O is your turn')
            turn_symbol = "O"
            count_turns += 1
        row = int(input("Enter a row (0, 1, or 2): "))
        column = int(input("Enter a column (0, 1, or 2): "))

        winner = user_in_board(turn_symbol,row,column)
        if winner:
            display_board(board)
            print(f"The winner is {turn_symbol}")
            break

    if count_turns == 9:
        print("There is no winners, it's a draw!")



# def playerO_input():
#     valid_symbols = {'O'}
#     player_O = input("Player O is your turn: ").upper()
#
#     while player_O not in valid_symbols:
#         print("You've introduced a wrong value.")
#         player_O = input("Please introduce the correct value 'O': ").upper()
#
#     rowO = int(input("Enter a row (0, 1, or 2): "))
#
#     columnO = int(input("Enter a column (0, 1, or 2): "))
#
#     userO_in_board(player_O,rowO,columnO)

def user_in_board(turn_symbol,row,column):
    if board[row][column] != ' ':
        print("The cell selected is not empty")
        player_input()
    else:
        board[row][column] = turn_symbol
    return (checking_winner())

# def userO_in_board(player_O,rowO,columnO):
#     if board[rowO][columnO] != ' ':
#         print("The cell selected is not empty")
#         playerO_input()
#     else:
#         board[rowO][columnO] = player_O
#         display_board(board)

def checking_rows():
    for r in board:
        if r [0] == r[1] and r[0] == r [2] and r[0] == "X":
            return (True)
            exit()
        elif r [0] == r [1] and r [0] == r [2] and r [0] == "O":
            return (True)
            exit()

def checking_columns():
    for c in range(0,3):
        if board [0][c] == board [1][c] and board [0][c] == board [2][c] and board [0][c] == "X":
            return (True)
            exit()
        elif board [0][c] == board [1][c] and board [0][c] == board [2][c] and board [0][c] == "O":
            return (True)
            exit()

def checking_diagonals():
        if board [0][0] == board [1][1] and board [0][0] == board [2][2] and board [0][0] == "X":
            return (True)
            exit()
        elif board [0][0] == board [1][1] and board [0][0] == board [2][2] and board [0][0] == "O":
            return (True)
            exit()
        elif board [0][2] == board [1][1] and board [0][2] == board [2][0] and board [0][2] == "X":
            return (True)
            exit()
        elif board [0][2] == board [1][1] and board [0][2] == board [2][0] and board [0][2] == "O":
            return (True)
            exit()

def checking_winner():

    if (checking_rows() or checking_diagonals() or checking_columns()):

        return (True)
    else:

        return (False)



# def playing_game():

    # for i in range(10):
    #     while player not in valid_symbols:
    #         print("You've introduced a wrong value.")
    #         player_X = input("Please introduce the correct value 'X': ").upper()



player_input()





