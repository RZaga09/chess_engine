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
row_comp = {  # translates row to array position
    7: '1',
    6: '2',
    5: '3',
    4: '4',
    3: '5',
    2: '6',
    1: '7',
    0: '8',
}

col_comp = {  # translates column to array position
    7: 'h',
    6: 'g',
    5: 'f',
    4: 'e',
    3: 'd',
    2: 'c',
    1: 'b',
    0: 'a',
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
        print("Input move with chess notation (i.e. a1)")
        move_from()
    # if square has no piece
    if board[row_notation.get(pos_from[1])][col_notation.get(pos_from[0])] == " ":
        print("Move not valid")
        move_from()
    # if piece is of the other player
    if (white == True and board[row_notation.get(pos_from[1])][col_notation.get(pos_from[0])].isupper() == False) or (white == False and board[row_notation.get(pos_from[1])][col_notation.get(pos_from[0])].isupper() == True): 
        print("Not your piece")
        move_from()

    move_to(pos_from)


def move_to(pos_from):
    global white 
    pos_to = input("To: ")
    # If square is invalid
    if len(pos_to) != 2 or pos_to[0] not in column or int(pos_to[1]) not in row:
        print("Input move with chess notation (i.e. a1")
        move_to(pos_from)
    # if square already has a piece of the same side
    if board[row_notation.get(pos_to[1])][col_notation.get(pos_to[0])] != " ":
        if (white == True and board[row_notation.get(pos_to[1])][col_notation.get(pos_to[0])].isupper() == True) or (white == False and board[row_notation.get(pos_to[1])][col_notation.get(pos_to[0])].isupper() == False):
            print("Own Piece")
            move_to(pos_from)

    # if piece is a knight
    if board[row_notation.get(pos_from[1])][col_notation.get(pos_from[0])] == 'N' or board[row_notation.get(pos_from[1])][col_notation.get(pos_from[0])] == 'n':
        possible_moves = [
            str(col_comp.get((col_notation.get(
                pos_from[0])) - 2)) + str(row_comp.get((row_notation.get(pos_from[1])) + 1)),
            str(col_comp.get((col_notation.get(
                pos_from[0])) - 2)) + str(row_comp.get((row_notation.get(pos_from[1])) - 1)),
            str(col_comp.get((col_notation.get(
                pos_from[0])) - 1)) + str(row_comp.get((row_notation.get(pos_from[1])) + 2)),
            str(col_comp.get((col_notation.get(
                pos_from[0])) - 1)) + str(row_comp.get((row_notation.get(pos_from[1])) - 2)),
            str(col_comp.get((col_notation.get(
                pos_from[0])) + 2)) + str(row_comp.get((row_notation.get(pos_from[1])) - 1)),
            str(col_comp.get((col_notation.get(
                pos_from[0])) + 2)) + str(row_comp.get((row_notation.get(pos_from[1])) + 1)),
            str(col_comp.get((col_notation.get(
                pos_from[0])) + 1)) + str(row_comp.get((row_notation.get(pos_from[1])) - 2)),
            str(col_comp.get((col_notation.get(
                pos_from[0])) + 1)) + str(row_comp.get((row_notation.get(pos_from[1])) + 2)),
        ]

        if len(possible_moves) == 0:
            print("Piece has no possible moves")
            move_from()

        if pos_to not in possible_moves:
            print("Move not valid")
            move_to(pos_from)

    # if piece is a bishop
    if board[row_notation.get(pos_from[1])][col_notation.get(pos_from[0])] == 'B' or board[row_notation.get(pos_from[1])][col_notation.get(pos_from[0])] == 'b':
        possible_moves = []
        move_filter = []
        move_add = []

        for i in range(1, 8):
            possible_moves.append(str(col_comp.get((col_notation.get(
                pos_from[0])) + i)) + str(row_comp.get((row_notation.get(pos_from[1])) + i)))
            possible_moves.append(str(col_comp.get((col_notation.get(
                pos_from[0])) - i)) + str(row_comp.get((row_notation.get(pos_from[1])) - i)))
            possible_moves.append(str(col_comp.get((col_notation.get(
                pos_from[0])) + i)) + str(row_comp.get((row_notation.get(pos_from[1])) - i)))
            possible_moves.append(str(col_comp.get((col_notation.get(
                pos_from[0])) - i)) + str(row_comp.get((row_notation.get(pos_from[1])) + i)))

        for j in range(1, 3):
            for i in possible_moves:
                if 'None' in i:
                    move_filter.append(i)

        for i in move_filter:
            if i in possible_moves:
                possible_moves.remove(i)

        for i in possible_moves:
            if board[row_notation.get(i[1])][col_notation.get(i[0])] != " ":
                move_filter.append(i)
                for j in possible_moves:
                    if column.index(i[0]) > column.index(pos_from[0]) and int(i[1]) > int(pos_from[1]):
                        if column.index(j[0]) > column.index(i[0]) and int(j[1]) > int(i[1]):
                            move_filter.append(j)
                    elif column.index(i[0]) < column.index(pos_from[0]) and int(i[1]) < int(pos_from[1]):
                        if column.index(j[0]) < column.index(i[0]) and int(j[1]) < int(i[1]):
                            move_filter.append(j)
                    elif column.index(i[0]) > column.index(pos_from[0]) and int(i[1]) < int(pos_from[1]):
                        if column.index(j[0]) > column.index(i[0]) and int(j[1]) <= int(i[1]):
                            move_filter.append(j)
                    elif column.index(i[0]) < column.index(pos_from[0]) and int(i[1]) > int(pos_from[1]):
                        if column.index(j[0]) < column.index(i[0]) and int(j[1]) > int(i[1]):
                            move_filter.append(j)

        for i in move_filter:
            if i in possible_moves:
                possible_moves.remove(i)

        for i in possible_moves:
            if i[1] > pos_from[1] and column.index(i[0]) > column.index(pos_from[0]):
                try:
                    compare = column[(col_notation.get(i[0]) + 1)] + str(int(i[1]) + 1)
                    if (white == True and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == False) or (white == False and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == True):
                        move_add.append(compare)
                except:
                    pass
            elif i[1] > pos_from[1] and column.index(i[0]) < column.index(pos_from[0]):
                try:
                    compare = column[(col_notation.get(i[0]) - 1)] + str(int(i[1]) + 1)
                    if (white == True and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == False) or (white == False and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == True):
                        move_add.append(compare)
                except:
                    pass
            elif i[1] < pos_from[1] and column.index(i[0]) > column.index(pos_from[0]):
                try:
                    compare = column[(col_notation.get(i[0]) + 1)] + str(int(i[1]) - 1)
                    if (white == True and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == False) or (white == False and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == True):
                        move_add.append(compare)
                except:
                    pass
            elif i[1] < pos_from[1] and column.index(i[0]) < column.index(pos_from[0]):
                try:
                    compare = column[(col_notation.get(i[0]) - 1)] + str(int(i[1]) - 1)
                    if (white == True and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == False) or (white == False and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == True):
                        move_add.append(compare)
                except:
                    pass

        for i in move_add:
            if i not in possible_moves:
                possible_moves.append(i)

        if len(possible_moves) == 0:
            print("Piece has no possible moves")
            move_from()

        print(possible_moves)

        if pos_to not in possible_moves:
            print("Move not valid")
            move_to(pos_from)

    # if piece is a rook
    if board[row_notation.get(pos_from[1])][col_notation.get(pos_from[0])] == 'R' or board[row_notation.get(pos_from[1])][col_notation.get(pos_from[0])] == 'r':
        possible_moves = []
        move_filter = []
        move_add = []

        for i in range(1, 8):
            possible_moves.append(str(col_comp.get((col_notation.get(
                pos_from[0])) + i)) + pos_from[1])
            possible_moves.append(str(col_comp.get((col_notation.get(
                pos_from[0])) - i)) + pos_from[1])
            possible_moves.append(pos_from[0] + str(row_comp.get(
                (row_notation.get(pos_from[1])) + i)))
            possible_moves.append(pos_from[0] + str(row_comp.get(
                (row_notation.get(pos_from[1])) - i)))

        for j in range(1, 3):
            for i in possible_moves:
                if 'None' in i:
                    move_filter.append(i)

        for i in move_filter:
            if i in possible_moves:
                possible_moves.remove(i)

        for i in possible_moves:
            if board[row_notation.get(i[1])][col_notation.get(i[0])] != " ":
                move_filter.append(i)
                for j in possible_moves:
                    if i[0] == pos_from[0] and int(i[1]) > int(pos_from[1]):
                        if int(j[1]) > int(i[1]):
                            move_filter.append(j)
                    elif i[0] == pos_from[0] and int(i[1]) < int(pos_from[1]):
                        if int(j[1]) < int(i[1]):
                            move_filter.append(j)
                    elif column.index(i[0]) > column.index(pos_from[0]) and int(i[1]) == int(pos_from[1]):
                        if column.index(j[0]) > column.index(i[0]):
                            move_filter.append(j)
                    elif column.index(i[0]) < column.index(pos_from[0]) and int(i[1]) == int(pos_from[1]):
                        if column.index(j[0]) < column.index(i[0]):
                            move_filter.append(j)

        for i in move_filter:
            if i in possible_moves:
                possible_moves.remove(i)

        for i in possible_moves:
            if pos_from[0] == i[0]:
                if i[1] > pos_from[1]:
                    try:
                        compare = i[0] + str(int(i[1]) + 1)
                        if (white == True and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == False) or (white == False and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == True):
                            move_add.append(compare)
                    except:
                        pass
                elif i[1] < pos_from[1]:
                    try:
                        compare = i[0] + str(int(i[1]) - 1)
                        if (white == True and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == False) or (white == False and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == True):
                            move_add.append(compare)
                    except:
                        pass
            elif pos_from[1] == i[1]:
                if column.index(i[0]) > column.index(pos_from[0]):
                    try:
                        compare = column[(col_notation.get(i[0]) + 1)] + i[1]
                        if (white == True and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == False) or (white == False and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == True):
                            move_add.append(compare)
                    except:
                        pass
                elif column.index(i[0]) < column.index(pos_from[0]):
                    try:
                        compare = column[(col_notation.get(i[0]) - 1)] + i[1]
                        if (white == True and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == False) or (white == False and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == True):
                            move_add.append(compare)
                    except:
                        pass

        for i in move_add:
            if i not in possible_moves:
                possible_moves.append(i)

        if len(possible_moves) == 0:
            print("Piece has no possible moves")
            move_from()

        if pos_to not in possible_moves:
            print("Move not valid")
            move_to(pos_from)

    # if piece is a queen
    if board[row_notation.get(pos_from[1])][col_notation.get(pos_from[0])] == 'Q' or board[row_notation.get(pos_from[1])][col_notation.get(pos_from[0])] == 'q':
        possible_moves = []
        move_filter = []
        move_add = []

        for i in range(1, 8):
            possible_moves.append(str(col_comp.get((col_notation.get(
                pos_from[0])) + i)) + pos_from[1])
            possible_moves.append(str(col_comp.get((col_notation.get(
                pos_from[0])) - i)) + pos_from[1])
            possible_moves.append(pos_from[0] + str(row_comp.get(
                (row_notation.get(pos_from[1])) + i)))
            possible_moves.append(pos_from[0] + str(row_comp.get(
                (row_notation.get(pos_from[1])) - i)))
            possible_moves.append(str(col_comp.get((col_notation.get(
                pos_from[0])) + i)) + str(row_comp.get((row_notation.get(pos_from[1])) + i)))
            possible_moves.append(str(col_comp.get((col_notation.get(
                pos_from[0])) - i)) + str(row_comp.get((row_notation.get(pos_from[1])) - i)))
            possible_moves.append(str(col_comp.get((col_notation.get(
                pos_from[0])) + i)) + str(row_comp.get((row_notation.get(pos_from[1])) - i)))
            possible_moves.append(str(col_comp.get((col_notation.get(
                pos_from[0])) - i)) + str(row_comp.get((row_notation.get(pos_from[1])) + i)))

        for j in range(1, 3):
            for i in possible_moves:
                if 'None' in i:
                    move_filter.append(i)

        for i in move_filter:
            if i in possible_moves:
                possible_moves.remove(i)

        for i in possible_moves:
            if board[row_notation.get(i[1])][col_notation.get(i[0])] != " ": 
                move_filter.append(i)

                for j in possible_moves:
                    if j[0] == i[0]:
                        if int(i[1]) > int(pos_from[1]):
                            if int(j[1]) > int(i[1]):
                                move_filter.append(j)
                        elif int(i[1]) < int(pos_from[1]):
                            if int(j[1]) < int(i[1]):
                                move_filter.append(j)
                    elif j[1] == i[1]:
                        if column.index(i[0]) > column.index(pos_from[0]):
                            if column.index(j[0]) > column.index(i[0]):
                                move_filter.append(j)
                        elif column.index(i[0]) < column.index(pos_from[0]):
                            if column.index(j[0]) < column.index(i[0]):
                                move_filter.append(j)
                    else:
                        if column.index(i[0]) > column.index(pos_from[0]) and int(i[1]) > int(pos_from[1]):
                            if column.index(j[0]) > column.index(i[0]) and int(j[1]) > int(i[1]):
                                move_filter.append(j)
                        elif column.index(i[0]) < column.index(pos_from[0]) and int(i[1]) < int(pos_from[1]):
                            if column.index(j[0]) < column.index(i[0]) and int(j[1]) < int(i[1]):
                                move_filter.append(j)
                        elif column.index(i[0]) > column.index(pos_from[0]) and int(i[1]) < int(pos_from[1]):
                            if column.index(j[0]) > column.index(i[0]) and int(j[1]) < int(i[1]):
                                move_filter.append(j)
                        elif column.index(i[0]) < column.index(pos_from[0]) and int(i[1]) > int(pos_from[1]):
                            if column.index(j[0]) < column.index(i[0]) and int(j[1]) > int(i[1]):
                                move_filter.append(j)

        for i in move_filter:
            if i in possible_moves:
                possible_moves.remove(i)

        for i in possible_moves:
            if pos_from[0] == i[0]:
                if i[1] > pos_from[1]:
                    try:
                        compare = i[0] + str(int(i[1]) + 1)
                        if (white == True and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == False) or (white == False and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == True):
                            move_add.append(compare)
                    except:
                        pass
                elif i[1] < pos_from[1]:
                    try:
                        compare = i[0] + str(int(i[1]) - 1)
                        if (white == True and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == False) or (white == False and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == True):
                            move_add.append(compare)
                    except:
                        pass
            elif pos_from[1] == i[1]:
                if column.index(i[0]) > column.index(pos_from[0]):
                    try:
                        compare = column[(col_notation.get(i[0]) + 1)] + i[1]
                        if (white == True and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == False) or (white == False and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == True):
                            move_add.append(compare)
                    except:
                        pass
                elif column.index(i[0]) < column.index(pos_from[0]):
                    try:
                        compare = column[(col_notation.get(i[0]) - 1)] + i[1]
                        if (white == True and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == False) or (white == False and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == True):
                            move_add.append(compare)
                    except:
                        pass
            else:
                if i[1] > pos_from[1] and column.index(i[0]) > column.index(pos_from[0]):
                    try:
                        compare = column[(col_notation.get(i[0]) + 1)] + str(int(i[1]) + 1)
                        if (white == True and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == False) or (white == False and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == True):
                            move_add.append(compare)
                    except:
                        pass
                elif i[1] > pos_from[1] and column.index(i[0]) < column.index(pos_from[0]):
                    try:
                        compare = column[(col_notation.get(i[0]) - 1)] + str(int(i[1]) + 1)
                        if (white == True and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == False) or (white == False and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == True):
                            move_add.append(compare)
                    except:
                        pass
                elif i[1] < pos_from[1] and column.index(i[0]) > column.index(pos_from[0]):
                    try:
                        compare = column[(col_notation.get(i[0]) + 1)] + str(int(i[1]) - 1)
                        if (white == True and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == False) or (white == False and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == True):
                            move_add.append(compare)
                    except:
                        pass
                elif i[1] < pos_from[1] and column.index(i[0]) < column.index(pos_from[0]):
                    try:
                        compare = column[(col_notation.get(i[0]) - 1)] + str(int(i[1]) - 1)
                        if (white == True and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == False) or (white == False and (board[row_notation.get(compare[1])][col_notation.get(compare[0])]).isupper() == True):
                            move_add.append(compare)
                    except:
                        pass

        for i in move_add:
            if i not in possible_moves:
                possible_moves.append(i)

        if len(possible_moves) == 0:
            print("Piece has no possible moves")
            move_from()

        if pos_to not in possible_moves:
            print("Move not valid")
            move_to(pos_from)

    # if piece is a white pawn
    if board[row_notation.get(pos_from[1])][col_notation.get(pos_from[0])] == 'P':
        possible_moves = [
            pos_from[0] +
            str(row_comp.get((row_notation.get(pos_from[1])) - 1)),
            pos_from[0] +
            str(row_comp.get((row_notation.get(pos_from[1])) - 2)),
        ]

        if int(pos_from[1]) != 2:
            del possible_moves[1]

        if pos_to not in possible_moves:
            print("Move not valid")
            move_to(pos_from)

    # if piece is a black pawn
    if board[row_notation.get(pos_from[1])][col_notation.get(pos_from[0])] == 'p':
        possible_moves = [
            pos_from[0] +
            str(row_comp.get((row_notation.get(pos_from[1])) + 1)),
            pos_from[0] +
            str(row_comp.get((row_notation.get(pos_from[1])) + 2)),
        ]

        if int(pos_from[1]) != 7:
            del possible_moves[1]

        if pos_to not in possible_moves:
            print("Move not valid")
            move_to(pos_from)

    # makes move
    board[row_notation.get(pos_to[1])][col_notation.get(
        pos_to[0])] = board[row_notation.get(pos_from[1])][col_notation.get(pos_from[0])]
    board[row_notation.get(pos_from[1])][col_notation.get(pos_from[0])] = ' '

    white = not white

    main()


starting_posiion()


def main():
    j = 0
    for i in range(8, 0, -1):  # shows board
        print(str(i) + '', board[j])
        j += 1
    print('    a    b    c    d    e    f    g    h')
    move_from()


main()
