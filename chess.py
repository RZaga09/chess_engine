board = [[" "] * 8 for i in range(8)]  # creates board

# chess pieces in unicode
# not used here due to lack of unicode support from various terminals
'''
K = u'\u2654' # W King
Q = u'\u2655' # W Queen
R = u'\u2656' # W Rook
B = u'\u2657' # W Bishop
N = u'\u2658' # W Knight
P = u'\u2659' # W Pawn
k = u'\u265A' # B King
q = u'\u265B' # B Queen
r = u'\u265C' # B Rook
b = u'\u265D' # B Bishop
n = u'\u265E' # B Knight
p = u'\u265F' # B Pawn
'''

to_chess_notation = {  # translates to chess notation
    0: "h",
    1: "g",
    2: "f",
    3: "e",
    4: "d",
    5: "c",
    6: "b",
    7: "a",
}

to_comp_notation = {  # translates to computer index
    "h": 0,
    "g": 1,
    "f": 2,
    "e": 3,
    "d": 4,
    "c": 5,
    "b": 6,
    "a": 7,
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


starting_posiion()
for i in board:  # shows board
    print(i)

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
