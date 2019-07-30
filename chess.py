board = [[' '] * 8 for i in range(8)]  # creates board

# Values for row and column
row = [1, 2, 3, 4, 5, 6, 7, 8]
column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

white = True  # Side to move

row_notation = {  # translates to row
    '1': 7,
    '2': 6,
    '3': 5,
    '4': 4,
    '5': 3,
    '6': 2,
    '7': 1,
    '8': 0,
}

col_notation = {  # translates to column
    "h": 7,
    "g": 6,
    "f": 5,
    "e": 4,
    "d": 3,
    "c": 2,
    "b": 1,
    "a": 0,
}


def starting_posiion():  # arranges starting position
    for i in range(8):  # arranges pawns
        board[1][i] = 'p'
        board[6][i] = 'P'
    # black pieces
    board[0][0] = board[0][7] = 'r'
    board[0][1] = board[0][6] = 'n'
    board[0][2] = board[0][5] = 'b'
    board[0][3] = 'q'
    board[0][4] = 'k'
    # white pieces
    board[7][0] = board[7][7] = 'R'
    board[7][1] = board[7][6] = 'N'
    board[7][2] = board[7][5] = 'B'
    board[7][3] = 'Q'
    board[7][4] = 'K'


def move_from():
    pos_from = input("From: ")
    # If square is invalid
    if len(pos_from) != 2 or pos_from[0] not in column or int(pos_from[1]) not in row:
        print("Input move with chess notation (i.e. a1")
        move_from()
    # if square has no piece
    if board[row_notation.get(pos_from[1])][col_notation.get(pos_from[0])] == " ":
        print("Move not valid")
        move_from()
    # sets square from to blank and returns piece to move
    return pos_from


def move_to():
    pos_to = input("To: ")
    # If square is invalid
    if len(pos_to) != 2 or pos_to[0] not in column or int(pos_to[1]) not in row:
        print("Input move with chess notation (i.e. a1")
        move_to()
    # if square already has a piece
    if board[row_notation.get(pos_to[1])][col_notation.get(pos_to[0])] != " ":
        print("Move not valid")
        move_to()
    return pos_to


starting_posiion()
while 1 == 1:
    for i in board:  # shows board
        print(i)
    pos_from = move_from()
    pos_to = move_to()
    board[row_notation.get(pos_to[1])][col_notation.get(
        pos_to[0])] = board[row_notation.get(pos_from[1])][col_notation.get(pos_from[0])]
    board[row_notation.get(pos_from[1])][col_notation.get(pos_from[0])] = ' '

# layout of the board
'''
8   0 = [0, 1, 2, 3, 4, 5, 6, 7] 
7   1 = [0, 1, 2, 3, 4, 5, 6, 7]
6   2 = [0, 1, 2, 3, 4, 5, 6, 7]
5   3 = [0, 1, 2, 3, 4, 5, 6, 7]
4   4 = [0, 1, 2, 3, 4, 5, 6, 7]
3   5 = [0, 1, 2, 3, 4, 5, 6, 7]
2   6 = [0, 1, 2, 3, 4, 5, 6, 7]
1   7 = [0, 1, 2, 3, 4, 5, 6, 7]
         a  b  c  d  e  f  g  h
'''
