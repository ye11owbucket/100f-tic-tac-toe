
def write(square,board,player):
  if board[square] == '-':
    board.pop(square)
    board.insert(square,player)
    return board
  elif 'O' == board[square]:
    return board
  elif 'X' == board[square]:
    return board

def read(square,board):
  if 'O' == board[square]:
    return 'O'
  elif 'X' == board[square]:
    return 'X'
  else:
    return None

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
        return 'no winner yet'


def tictact0e():
    board = ['-','-','-','-','-','-','-','-','-']
    while True:
        print('r to read\nw to write\nc to check if win')
        choice = input(': ')
        if choice == 'r':
            square = int(input("square"))
            print(read(square,board))
        if choice == 'w':
            player = input("player")
            square = int(input("square"))
            write(square,board,player)
        if choice == 'c':
            winner = whoWins(board)
            if winner == 'X':
                print('X has won!')
                break
            if winner =='O':
                print('O has won!')
                break
            else:
                print('nobody has won yet :(')
        if choice == 'p':
            print(board)

 

tictact0e()