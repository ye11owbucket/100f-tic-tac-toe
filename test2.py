def whoWins(board):
    a = board[0]
    b = board[1]
    c = board[2]
    d = board[3]
    e = board[4]
    f = board[5]
    g = board[6]
    h = board[7]
    i = board[8]
    ### O's
    if (a+b+c) == 'OOO':
        return 'O'
    if (a+e+i) == 'OOO':
        return 'O'
    if (a+d+g) == 'OOO':
        return 'O'
    if (d+e+f) == 'OOO':
        return 'O'
    if (g+h+i) == 'OOO':
        return 'O'
    if (g+e+c) == 'OOO':
        return 'O'
    if (b+e+h) == 'OOO':
        return 'O'
    if (c+f+i) == 'OOO':
        return 'O'
    ### X's
    if (a+b+c) == 'XXX':
        return 'X'
    if (a+e+i) == 'XXX':
        return 'X'
    if (a+d+g) == 'XXX':
        return 'X'
    if (d+e+f) == 'XXX':
        return 'X'
    if (g+h+i) == 'XXX':
        return 'X'
    if (g+e+c) == 'XXX':
        return 'X'
    if (b+e+h) == 'XXX':
        return 'X'
    if (c+f+i) == 'XXX':
        return 'X'
    else:
        return None



board = [ 'O','O','O',0,'X',0,'O','O','X']
print(whoWins(board))
