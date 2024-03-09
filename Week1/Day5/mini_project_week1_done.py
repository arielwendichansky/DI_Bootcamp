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

def playerX_input():
    valid_symbols = {'X'}
    player_X = input("Player X is your turn: ").upper()

    while player_X not in valid_symbols:
        print("You've introduced a wrong value.")
        player_X = input("Please introduce the correct value 'X': ").upper()

    rowX = int(input("Enter a row (0, 1, or 2): "))

    columnX = int(input("Enter a column (0, 1, or 2): "))

    userX_in_board(player_X,rowX,columnX)


def playerO_input():
    valid_symbols = {'O'}
    player_O = input("Player O is your turn: ").upper()

    while player_O not in valid_symbols:
        print("You've introduced a wrong value.")
        player_O = input("Please introduce the correct value 'O': ").upper()

    rowO = int(input("Enter a row (0, 1, or 2): "))

    columnO = int(input("Enter a column (0, 1, or 2): "))

    userO_in_board(player_O,rowO,columnO)

def userX_in_board(player_X,rowX,columnX):
    if board[rowX][columnX] != ' ':
        print("The cell selected is not empty")
        playerX_input()
    else:
        board[rowX][columnX] = player_X
        display_board(board)

def userO_in_board(player_O,rowO,columnO):
    if board[rowO][columnO] != ' ':
        print("The cell selected is not empty")
        playerO_input()
    else:
        board[rowO][columnO] = player_O
        display_board(board)

def checking_rows():
    for r in board:
        if r [0] == r[1] and r[0] == r [2] and r[0] == "X":
            print("User X wins")
            exit()
        elif r [0] == r [1] and r [0] == r [2] and r [0] == "X":
            print("User O wins")
            exit()

def checking_columns():
    for c in range(0,3):
        if board [0][c] == board [1][c] and board [0][c] == board [2][c] and board [0][c] == "X":
            print("User X wins")
            exit()
        elif board [0][c] == board [1][c] and board [0][c] == board [2][c] and board [0][c] == "O":
            print("User O wins")
            exit()

def checking_diagonals():
        if board [0][0] == board [1][1] and board [0][0] == board [2][2] and board [0][0] == "X":
            print("User X wins")
            exit()
        elif board [0][0] == board [1][1] and board [0][0] == board [2][2] and board [0][0] == "O":
            print("User O wins")
            exit()
        elif board [0][2] == board [1][1] and board [0][2] == board [2][0] and board [0][2] == "X":
            print("User X wins")
            exit()
        elif board [0][2] == board [1][1] and board [0][2] == board [2][0] and board [0][2] == "O":
            print("User O wins")
            exit()

def checking_winner():
    checking_rows()
    checking_columns()
    checking_diagonals()

def playing_game():
    playerX_input()
    playerO_input()
    playerX_input()
    playerO_input()
    playerX_input()
    checking_winner()
    playerO_input()
    checking_winner()
    playerX_input()
    checking_winner()
    playerO_input()
    checking_winner()
    playerX_input()
    print("There is no winners, it's a draw!")

display_board(board)
playing_game()



