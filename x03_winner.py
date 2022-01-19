#!python3

"""
Create a function that will determine if one person is the winner (has 3 in a row)
inputs:
list board : the list that contains the board data

return:
str 'X' if X is the winner
str 'O' if O is the winner
None if there is no winner
"""

def whoWins(board):
    kill = 0
    if kill in board:
      for i in board:
        x = board.index(kill)
        board.pop(x)
        board.insert(x,'-')
        if kill not in board:
          break
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

def main():
  board = [ 'O','X',0,'X','O',0,'X',0,'O']
  assert whoWins(board) == 'O'
  board = [ 'X','O',0,'X','O','X','O','O','X']
  assert whoWins(board) == 'O'
  board = [ 'X','O',0,'X','X','O','O','X','O']
  assert whoWins(board) == None
  board = [ 'X','O',0,'X','X','X','O','O','X']
  assert whoWins(board) == 'X'

if __name__ == "__main__":
  main()
