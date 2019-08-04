# create board
board = []
for i in range(64):
    board.append(' ')

white = True
white_in_check = False
black_in_check = False
white_king_pos = 0
black_king_pos = 0
moves = []

arr_notation = {  # translates chess notation to array notation
    'a8': 0,
    'b8': 1,
    'c8': 2,
    'd8': 3,
    'e8': 4,
    'f8': 5,
    'g8': 6,
    'h8': 7,
    'a7': 8,
    'b7': 9,
    'c7': 10,
    'd7': 11,
    'e7': 12,
    'f7': 13,
    'g7': 14,
    'h7': 15,
    'a6': 16,
    'b6': 17,
    'c6': 18,
    'd6': 19,
    'e6': 20,
    'f6': 21,
    'g6': 22,
    'h6': 23,
    'a5': 24,
    'b5': 25,
    'c5': 26,
    'd5': 27,
    'e5': 28,
    'f5': 29,
    'g5': 30,
    'h5': 31,
    'a4': 32,
    'b4': 33,
    'c4': 34,
    'd4': 35,
    'e4': 36,
    'f4': 37,
    'g4': 38,
    'h4': 39,
    'a3': 40,
    'b3': 41,
    'c3': 42,
    'd3': 43,
    'e3': 44,
    'f3': 45,
    'g3': 46,
    'h3': 47,
    'a2': 48,
    'b2': 49,
    'c2': 50,
    'd2': 51,
    'e2': 52,
    'f2': 53,
    'g2': 54,
    'h2': 55,
    'a1': 56,
    'b1': 57,
    'c1': 58,
    'd1': 59,
    'e1': 60,
    'f1': 61,
    'g1': 62,
    'h1': 63,
}

chess_notation = {
    0: 'a8',
    1: 'b8',
    2: 'c8',
    3: 'd8',
    4: 'e8',
    5: 'f8',
    6: 'g8',
    7: 'h8',
    8: 'a7',
    9: 'b7',
    10: 'c7',
    11: 'd7',
    12: 'e7',
    13: 'f7',
    14: 'g7',
    15: 'h7',
    16: 'a6',
    17: 'b6',
    18: 'c6',
    19: 'd6',
    20: 'e6',
    21: 'f6',
    22: 'g6',
    23: 'h6',
    24: 'a5',
    25: 'b5',
    26: 'c5',
    27: 'd5',
    28: 'e5',
    29: 'f5',
    30: 'g5',
    31: 'h5',
    32: 'a4',
    33: 'b4',
    34: 'c4',
    35: 'd4',
    36: 'e4',
    37: 'f4',
    38: 'g4',
    39: 'h4',
    40: 'a3',
    41: 'b3',
    42: 'c3',
    43: 'd3',
    44: 'e3',
    45: 'f3',
    46: 'g3',
    47: 'h3',
    48: 'a2',
    49: 'b2',
    50: 'c2',
    51: 'd2',
    52: 'e2',
    53: 'f2',
    54: 'g2',
    55: 'h2',
    56: 'a1',
    57: 'b1',
    58: 'c1',
    59: 'd1',
    60: 'e1',
    61: 'f1',
    62: 'g1',
    63: 'h1',
}

# starting position


def starting_pos():
    # black pieces
    board[0] = board[7] = 'r'
    board[1] = board[6] = 'n'
    board[2] = board[5] = 'b'
    board[3] = 'q'
    board[4] = 'k'
    for i in range(8, 16):
        board[i] = 'p'
    # white pieces
    board[56] = board[63] = 'R'
    board[57] = board[62] = 'N'
    board[58] = board[61] = 'B'
    board[59] = 'Q'
    board[60] = 'K'
    for i in range(48, 56):
        board[i] = 'P'

# check if white is in check


def white_check():
    global white_king_pos
    global white_in_check
    white_pieces = ['K', 'Q', 'B', 'R', 'N', 'P']
    black_pieces = ['k', 'q', 'b', 'r', 'n', 'p']
    for i in range(64):
        if board[i] == 'K':
            white_king_pos = i
            break
    if white_king_pos - 7 == 'p' and white_king_pos != 7 and white_king_pos != 15 and white_king_pos != 23 and white_king_pos != 31 and white_king_pos != 39 and white_king_pos != 47 and white_king_pos != 55 and white_king_pos != 63:
        white_in_check = True

    if white_king_pos - 9 == 'p' and white_king_pos != 0 and white_king_pos != 8 and white_king_pos != 16 and white_king_pos != 24 and white_king_pos != 32 and white_king_pos != 40 and white_king_pos != 48 and white_king_pos != 56:
        white_in_check = True

    if white_king_pos != 0:
        try:
            if board[white_king_pos + 15] == 'n':
                white_in_check = True
        except IndexError:
            pass
    if white_king_pos != 63:
        try:
            if board[white_king_pos - 15] == 'n' and (white_king_pos - 15) >= 0:
                white_in_check = True
        except IndexError:
            pass
    if white_king_pos != 7:
        try:
            if board[white_king_pos + 17] == 'n':
                white_in_check = True
        except IndexError:
            pass
    if white_king_pos != 56:
        try:
            if board[white_king_pos - 17] == 'n' and (white_king_pos - 17) >= 0:
                white_in_check = True
        except IndexError:
            pass
    if white_king_pos != 7 and white_king_pos != 6:
        try:
            if board[white_king_pos + 10] == 'n':
                white_in_check = True
        except IndexError:
            pass
    if white_king_pos != 56 and white_king_pos != 57:
        try:
            if board[white_king_pos - 10] == 'n' and (white_king_pos - 10) >= 0:
                white_in_check = True
        except IndexError:
            pass
    if white_king_pos != 0 and white_king_pos != 56 and white_king_pos != 57:
        try:
            if board[white_king_pos + 6] == 'n':
                white_in_check = True
        except IndexError:
            pass
    if white_king_pos != 7 and white_king_pos != 63 and white_king_pos != 62:
        try:
            if board[white_king_pos - 6] == 'n' and (white_king_pos - 6) >= 0:
                white_in_check = True
        except IndexError:
            pass

    if white_in_check == False:
        i = white_king_pos
        while 1 == 1:
            i += 9
            if i > 63:
                break
            if board[i] == 'q' or board[i] == 'b':
                white_in_check = True
                break
            elif i >= 56 or i == 7 or i == 15 or i == 23 or i == 31 or i == 39 or i == 47 or i == 55 or i in black_pieces or i in white_pieces:
                break
        i = white_king_pos
        while 1 == 1:
            i += 8
            if i > 63:
                break
            if board[i] == 'q' or board[i] == 'r':
                white_in_check = True
                break
            elif i >= 56 or i in black_pieces or i in white_pieces:
                break
        i = white_king_pos
        while 1 == 1:
            i += 7
            if i > 63:
                break
            if board[i] == 'q' or board[i] == 'b':
                white_in_check = True
                break
            elif i >= 56 or i == 0 or i == 8 or i == 16 or i == 24 or i == 32 or i == 40 or i == 48 or i in black_pieces or i in white_pieces:
                break
        i = white_king_pos
        while 1 == 1:
            i += 1
            if i > 63:
                break
            if board[i] == 'q' or board[i] == 'r':
                white_in_check = True
                break
            elif i == 7 or i == 15 or i == 23 or i == 31 or i == 39 or i == 47 or i == 55 or i == 63 or i in black_pieces or i in white_pieces:
                break

        i = white_king_pos
        while 1 == 1:
            i -= 9
            if i < 0:
                break
            if board[i] == 'q' or board[i] == 'b':
                white_in_check = True
                break
            elif i <= 7 or i == 0 or i == 8 or i == 16 or i == 24 or i == 32 or i == 40 or i == 48 or i == 56 or i in black_pieces or i in white_pieces:
                break
        i = white_king_pos
        while 1 == 1:
            i -= 8
            if i < 0:
                break
            if board[i] == 'q' or board[i] == 'r':
                white_in_check = True
                break
            elif i <= 7 or i in black_pieces or i in white_pieces:
                break
        i = white_king_pos
        while 1 == 1:
            i -= 7
            if i < 0:
                break
            if board[i] == 'q' or board[i] == 'b':
                white_in_check = True
                break
            elif i <= 7 or i == 15 or i == 23 or i == 31 or i == 39 or i == 47 or i == 55 or i == 63 or i in black_pieces or i in white_pieces:
                break
        i = white_king_pos
        while 1 == 1:
            i -= 1
            if i < 0:
                break
            if board[i] == 'q' or board[i] == 'r':
                white_in_check = True
                break
            elif i == 0 or i == 8 or i == 16 or i == 24 or i == 32 or i == 40 or i == 48 or i == 56 or i in black_pieces or i in white_pieces:
                break

# check if black is in check


def black_check():
    global black_king_pos
    global black_in_check
    white_pieces = ['K', 'Q', 'B', 'R', 'N', 'P']
    black_pieces = ['k', 'q', 'b', 'r', 'n', 'p']
    for i in range(64):
        if board[i] == 'k':
            black_king_pos = i
            break

    if black_king_pos + 7 == 'P' and black_king_pos != 0 and black_king_pos != 8 and black_king_pos != 16 and black_king_pos != 24 and black_king_pos != 32 and black_king_pos != 40 and black_king_pos != 48 and black_king_pos != 56:
        black_in_check = True

    if black_king_pos + 9 == 'P' and black_king_pos != 7 and black_king_pos != 15 and black_king_pos != 23 and black_king_pos != 31 and black_king_pos != 39 and black_king_pos != 47 and black_king_pos != 55 and black_king_pos != 63:
        black_in_check = True

    if black_king_pos != 0:
        try:
            if board[black_king_pos + 15] == 'N':
                black_in_check = True
        except IndexError:
            pass
    if black_king_pos != 63:
        try:
            if board[black_king_pos - 15] == 'N' and (black_king_pos - 15) >= 0:
                black_in_check = True
        except IndexError:
            pass
    if black_king_pos != 7:
        try:
            if board[black_king_pos + 17] == 'N':
                black_in_check = True
        except IndexError:
            pass
    if black_king_pos != 56:
        try:
            if board[black_king_pos - 17] == 'N' and (black_king_pos - 17) >= 0:
                black_in_check = True
        except IndexError:
            pass
    if black_king_pos != 7 and black_king_pos != 6:
        try:
            if board[black_king_pos + 10] == 'N':
                black_in_check = True
        except IndexError:
            pass
    if black_king_pos != 56 and black_king_pos != 57:
        try:
            if board[black_king_pos - 10] == 'N' and (black_king_pos - 10) >= 0:
                black_in_check = True
        except IndexError:
            pass
    if black_king_pos != 0 and black_king_pos != 56 and black_king_pos != 57:
        try:
            if board[black_king_pos + 6] == 'N':
                black_in_check = True
        except IndexError:
            pass
    if black_king_pos != 7 and black_king_pos != 63 and black_king_pos != 62:
        try:
            if board[black_king_pos - 6] == 'N' and (black_king_pos - 6) >= 0:
                black_in_check = True
        except IndexError:
            pass

    if black_in_check == False:
        i = black_king_pos
        while 1 == 1:
            i += 9
            if i > 63:
                break
            if board[i] == 'Q' or board[i] == 'B':
                black_in_check = True
                break
            elif i >= 56 or i == 7 or i == 15 or i == 23 or i == 31 or i == 39 or i == 47 or i == 55 or i in black_pieces or i in white_pieces:
                break
        i = black_king_pos
        while 1 == 1:
            i += 8
            if i > 63:
                break
            if board[i] == 'Q' or board[i] == 'R':
                black_in_check = True
                break
            elif i >= 56 or i in black_pieces or i in white_pieces:
                break
        i = black_king_pos
        while 1 == 1:
            i += 7
            if i > 63:
                break
            if board[i] == 'Q' or board[i] == 'B':
                black_in_check = True
                break
            elif i >= 56 or i == 0 or i == 8 or i == 16 or i == 24 or i == 32 or i == 40 or i == 48 or i in black_pieces or i in white_pieces:
                break
        i = black_king_pos
        while 1 == 1:
            i += 1
            if i > 63:
                break
            if board[i] == 'Q' or board[i] == 'R':
                black_in_check = True
                break
            elif i == 7 or i == 15 or i == 23 or i == 31 or i == 39 or i == 47 or i == 55 or i == 63 or i in black_pieces or i in white_pieces:
                break

        i = black_king_pos
        while 1 == 1:
            i -= 9
            if i < 0:
                break
            if board[i] == 'Q' or board[i] == 'B':
                black_in_check = True
                break
            elif i <= 7 or i == 0 or i == 8 or i == 16 or i == 24 or i == 32 or i == 40 or i == 48 or i == 56 or i in black_pieces or i in white_pieces:
                break
        i = black_king_pos
        while 1 == 1:
            i -= 8
            if i < 0:
                break
            if board[i] == 'Q' or board[i] == 'R':
                black_in_check = True
                break
            elif i <= 7 or i in black_pieces or i in white_pieces:
                break
        i = black_king_pos
        while 1 == 1:
            i -= 7
            if i < 0:
                break
            if board[i] == 'Q' or board[i] == 'B':
                black_in_check = True
                break
            elif i <= 7 or i == 15 or i == 23 or i == 31 or i == 39 or i == 47 or i == 55 or i == 63 or i in black_pieces or i in white_pieces:
                break
        i = black_king_pos
        while 1 == 1:
            i -= 1
            if i < 0:
                break
            if board[i] == 'Q' or board[i] == 'R':
                black_in_check = True
                break
            elif i == 0 or i == 8 or i == 16 or i == 24 or i == 32 or i == 40 or i == 48 or i == 56 or i in black_pieces or i in white_pieces:
                break


def possible_moves():
    global white
    global moves
    moves = []
    own_pieces = []
    opp_pieces = []
    has_player = []
    has_enemy = []
    no_piece = []
    if white == True:
        own_pieces = ['K', 'Q', 'B', 'R', 'N', 'P']
        opp_pieces = ['k', 'q', 'b', 'r', 'n', 'p']
    else:
        own_pieces = ['k', 'q', 'b', 'r', 'n', 'p']
        opp_pieces = ['K', 'Q', 'B', 'R', 'N', 'P']

    for i in range(64):
        if board[i] in own_pieces:
            has_player.append(i)
        elif board[i] in opp_pieces:
            has_enemy.append(i)
        else:
            no_piece.append(i)

    for i in (has_player):
        # King
        if board[i] == 'K' or board[i] == 'k':
            if i - 9 not in has_player:
                moves.append(str(chess_notation.get(i)) +
                             str(chess_notation.get(i - 9)))
            if i - 8 not in has_player:
                moves.append(str(chess_notation.get(i)) +
                             str(chess_notation.get(i - 8)))
            if i - 7 not in has_player:
                moves.append(str(chess_notation.get(i)) +
                             str(chess_notation.get(i - 7)))
            if i - 1 not in has_player:
                moves.append(str(chess_notation.get(i)) +
                             str(chess_notation.get(i - 1)))
            if i + 1 not in has_player:
                moves.append(str(chess_notation.get(i)) +
                             str(chess_notation.get(i + 1)))
            if i + 7 not in has_player:
                moves.append(str(chess_notation.get(i)) +
                             str(chess_notation.get(i + 7)))
            if i + 8 not in has_player:
                moves.append(str(chess_notation.get(i)) +
                             str(chess_notation.get(i + 8)))
            if i + 9 not in has_player:
                moves.append(str(chess_notation.get(i)) +
                             str(chess_notation.get(i + 9)))

        # Rook
        if board[i] == 'R' or board[i] == 'r':
            j = i
            while 1 == 1:
                j += 1
                if j not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(j)))
                else:
                    break
                if j == 7 or j == 15 or j == 23 or j == 31 or j == 39 or j == 47 or j == 55 or j >= 63 or j in has_enemy or j == 'k' or j == 'K':
                    break
            j = i
            while 1 == 1:
                j -= 1
                if j not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(j)))
                else:
                    break
                if j == 0 or j == 8 or j == 16 or j == 24 or j == 32 or j == 40 or j == 48 or j == 56 or j in has_enemy or j == 'k' or j == 'K':
                    break
            j = i
            while 1 == 1:
                j += 8
                if j not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(j)))
                else:
                    break
                if j >= 56 or j in has_enemy or j == 'k' or j == 'K':
                    break
            j = i
            while 1 == 1:
                j -= 8
                if j not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(j)))
                else:
                    break
                if j <= 7 or j in has_enemy or j == 'k' or j == 'K':
                    break

        # Bishop
        if board[i] == 'B' or board[i] == 'b':
            j = i
            while 1 == 1:
                j += 7
                if j not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(j)))
                else:
                    break
                if j >= 56 or j == 48 or j == 40 or j == 32 or j == 24 or j == 16 or j == 8 or j == 0 or j in has_enemy or j == 'k' or j == 'K':
                    break
            j = i
            while 1 == 1:
                j -= 7
                if j not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(j)))
                else:
                    break
                if (j >= 0 and j <= 7) or j == 15 or j == 23 or j == 31 or j == 39 or j == 47 or j == 55 or j == 63 or j in has_enemy or j == 'k' or j == 'K':
                    break
            j = i
            while 1 == 1:
                j += 9
                if j not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(j)))
                else:
                    break
                if j >= 55 or j == 7 or j == 15 or j == 23 or j == 31 or j == 39 or j == 47 or j in has_enemy or j == 'k' or j == 'K':
                    break
            j = i
            while 1 == 1:
                j -= 9
                if j not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(j)))
                else:
                    break
                if j <= 8 or j == 16 or j == 24 or j == 32 or j == 40 or j == 48 or j == 56 or j in has_enemy or j == 'k' or j == 'K':
                    break

        # Queen
        if board[i] == 'Q' or board[i] == 'q':
            j = i
            while 1 == 1:
                j += 7
                if j not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(j)))
                else:
                    break
                if j >= 56 or j == 48 or j == 40 or j == 32 or j == 24 or j == 16 or j == 8 or j == 0 or j in has_enemy or j == 'k' or j == 'K':
                    break
            j = i
            while 1 == 1:
                j -= 7
                if j not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(j)))
                else:
                    break
                if (j >= 0 and j <= 7) or j == 15 or j == 23 or j == 31 or j == 39 or j == 47 or j == 55 or j == 63 or j in has_enemy or j == 'k' or j == 'K':
                    break
            j = i
            while 1 == 1:
                j += 9
                if j not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(j)))
                else:
                    break
                if j >= 55 or j == 7 or j == 15 or j == 23 or j == 31 or j == 39 or j == 47 or j in has_enemy or j == 'k' or j == 'K':
                    break
            j = i
            while 1 == 1:
                j -= 9
                if j not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(j)))
                else:
                    break
                if j <= 8 or j == 16 or j == 24 or j == 32 or j == 40 or j == 48 or j == 56 or j in has_enemy or j == 'k' or j == 'K':
                    break
            j = i
            while 1 == 1:
                j += 1
                if j not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(j)))
                else:
                    break
                if j == 7 or j == 15 or j == 23 or j == 31 or j == 39 or j == 47 or j == 55 or j == 63 or j in has_enemy or j == 'k' or j == 'K':
                    break
            j = i
            while 1 == 1:
                j -= 1
                if j not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(j)))
                else:
                    break
                if j == 0 or j == 8 or j == 16 or j == 24 or j == 32 or j == 40 or j == 48 or j == 56 or j in has_enemy or j == 'k' or j == 'K':
                    break
            j = i
            while 1 == 1:
                j += 8
                if j not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(j)))
                else:
                    break
                if j >= 56 or j in has_enemy or j == 'k' or j == 'K':
                    break
            j = i
            while 1 == 1:
                j -= 8
                if j not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(j)))
                else:
                    break
                if j <= 7 or j in has_enemy or j == 'k' or j == 'K':
                    break

        # Knight
        if board[i] == 'N' or board[i] == 'n':
            if i != 0:
                if i + 15 not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(i + 15)))
                else:
                    pass
            if i != 63:
                if i - 15 not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(i - 15)))
                else:
                    pass
            if i != 7:
                if i + 17 not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(i + 17)))
                else:
                    pass
            if i != 56:
                if i - 17 not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(i - 17)))
                else:
                    pass
            if i != 7 and i != 6:
                if i + 10 not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(i + 10)))
                else:
                    pass
            if i != 56 and i != 57:
                if i - 10 not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(i - 10)))
                else:
                    pass
            if i != 0 and i != 56 and i != 57:
                if i + 6 not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(i + 6)))
                else:
                    pass
            if i != 7 and i != 63 and i != 62:
                if i - 6 not in has_player:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(i - 6)))
                else:
                    pass

        # White Pawn
        if board[i] == 'P':
            if i - 8 not in has_player:
                moves.append(str(chess_notation.get(i)) +
                             str(chess_notation.get(i - 8)))
                if i >= 48:
                    if i - 16 not in has_player:
                        moves.append(str(chess_notation.get(i)) +
                                     str(chess_notation.get(i - 16)))
            else:
                pass

            if i != 7 and i != 15 and i != 23 and i != 31 and i != 39 and i != 47 and i != 55 and i != 63:
                if i - 7 in has_enemy:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(i - 7)))
                else:
                    pass
            if i != 0 and i != 8 and i != 16 and i != 24 and i != 32 and i != 40 and i != 48 and i != 56:
                if i - 9 in has_enemy:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(i - 9)))
                else:
                    pass

        # Black Pawn
        if board[i] == 'p':
            if i + 8 not in has_player:
                moves.append(str(chess_notation.get(i)) +
                             str(chess_notation.get(i + 8)))
                if i <= 15:
                    if i + 16 not in has_player:
                        moves.append(str(chess_notation.get(i)) +
                                     str(chess_notation.get(i + 16)))
            else:
                pass
            if i != 0 and i != 8 and i != 16 and i != 24 and i != 32 and i != 40 and i != 48 and i != 56:
                if i + 7 in has_enemy:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(i + 7)))
                else:
                    pass
            if i != 7 and i != 15 and i != 23 and i != 31 and i != 39 and i != 47 and i != 55 and i != 63:
                if i + 9 in has_enemy:
                    moves.append(str(chess_notation.get(i)) +
                                 str(chess_notation.get(i + 9)))
                else:
                    pass

    for i in range(30):
        for i in moves:
            if 'None' in i:
                moves.remove(i)

    print(moves)


# shows board on command line


def show():
    row8 = []
    row7 = []
    row6 = []
    row5 = []
    row4 = []
    row3 = []
    row2 = []
    row1 = []
    for i in range(64):
        if i < 8:
            row8.append(board[i])
        elif i < 16:
            row7.append(board[i])
        elif i < 24:
            row6.append(board[i])
        elif i < 32:
            row5.append(board[i])
        elif i < 40:
            row4.append(board[i])
        elif i < 48:
            row3.append(board[i])
        elif i < 56:
            row2.append(board[i])
        elif i < 64:
            row1.append(board[i])

    print(row8)
    print(row7)
    print(row6)
    print(row5)
    print(row4)
    print(row3)
    print(row2)
    print(row1)


starting_pos()


def main():
    global white_in_check
    global black_in_check
    white_check()
    black_check()
    show()
    possible_moves()
    if white_in_check == True:
        print("WHITE IN CHECK")
    if black_in_check == True:
        print("BLACK IN CHECK")
    move = input('Move: ')
    for i in moves:
        if move == i:
            board[arr_notation.get(str(i[2:4]))
                  ] = board[arr_notation.get(str(i[0:2]))]
            board[arr_notation.get(str(i[0:2]))] = ' '
            break
    white_in_check = False
    black_in_check = False
    main()


main()

'''
Layout of board
8   [ 0,  1,  2,  3,  4,  5,  6,  7]
7   [ 8,  9, 10, 11, 12, 13, 14, 15]
6   [16, 17, 18, 19, 20, 21, 22, 23]
5   [24, 25, 26, 27, 28, 29, 30, 31]
4   [32, 33, 34, 35, 36, 37, 38, 39]
3   [40, 41, 42, 43, 44, 45, 46, 47]
2   [48, 49, 50, 51, 52, 53, 54, 55]
1   [56, 57, 58, 59, 60, 61, 62, 63]
      a   b   c   d   e   f   g   h
'''
