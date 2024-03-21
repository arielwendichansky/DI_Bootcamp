welcome_message = print("Welcome to TIC TAC TOE!")
matrix = [["    " for column in range(3)] for row in range(5)]
moves = []
played_turn = 0
# def create_board():
#     print("*"*17)
#     line1 = list(" "*5+"|"+" "*3+"|"+" "*5)
#     print(line1)
#     print ("*"+" "*2+"-"*3+"|"+"-"*3+"|"+"-"*3+" "*2+"*")
#     line2 = list(" "*5+"|"+" "*3+"|"+" "*5+"*")
#     print(line2)
#     print ("*"+" "*2+"-"*3+"|"+"-"*3+"|"+"-"*3+" "*2+"*")
#     line3 = list(" "*5+"|"+" "*3+"|"+" "*5+"*")
#     print("*"*17)
#     print(line3)

def display_board(matrix):
    separate_lines = "----"
    print("*" * 17)
    for i,row in enumerate(matrix):
        print("*", end="")
        for index,element in enumerate(row):
            if i == 1 and index == 0:
                print(separate_lines,end="|")
            elif i == 1 and index == 1:
                print(separate_lines,end="|")
            elif i == 1 and index == 2:
                print(separate_lines,"*")
            elif i == 3 and index == 0:
                print(separate_lines,end="|")
            elif i == 3 and index == 1:
                print(separate_lines,end="|")
            elif i == 3 and index == 2:
                print(separate_lines,"*")
            elif index == 0:
                print(element,end="|")
            elif index == 1:
                print(element, end="|")
            elif index == 2:
                print(element,"*")
    print("*" * 17)

display_board(matrix)

# def player_input(*args):
# #     played_turns = 0
# #     if played_turns <= 9:
#         player = input("It's your turn, introduce 'X' or 'O': ")
# #          played_turns += 1
#         while player.upper() not in ('X', 'O'):
#             print("You've introduce a wrong value. ")
#             player = input("Please introduce a correct value 'X' or 'O' ")
#             continue
#         row = input("Enter a row: ")
#         while not row.isdigit():
#             print("You've introduce a wrong value. ")
#             row = input("Enter a row: ")
#         column = input("Enter a column: ")
#         while not column.isdigit():
#             print("You've introduce a wrong value. ")
#             column = input("Enter a row: ")
#         return player.upper(),int(row),int(column)
# player_input()

def player_input(played_turn):
    max_turns = 9

    if played_turn == max_turns:
        print("Maximum turns reached. Restarting the game.")
        played_turn = 0

    valid_symbols = {'X', 'O'}
    player = input("It's your turn, introduce 'X' or 'O': ").upper()

    while player not in valid_symbols:
        print("You've introduced a wrong value.")
        player = input("Please introduce a correct value 'X' or 'O': ").upper()

    row = input("Enter a row (0, 2, or 4): ")
    while not row.isdigit() or int(row) not in range(5):
        print("You've introduced a wrong value.")
        row = input("Enter a row (0, 2, or 4): ")

    column = input("Enter a column (0, 1, or 2): ")
    while not column.isdigit() or int(column) not in range(3):
        print("You've introduced a wrong value.")
        column = input("Enter a column (0, 1, or 2): ")

    return player, int(row), int(column), played_turn + 1


def modify_board(display_board, row, column, player):
    board_changes = [row[:] for row in display_board]
    board_changes[row][column] = f"  {player} "
    return board_changes

while played_turn < 10:
    player, row, column, played_turns = player_input(played_turn)
    board_changes = modify_board(matrix, row, column, player)
    moves.append([row[:] for row in board_changes])

    for move in moves:
        display_board(move)

played_turn = 0
moves = []