def read(square,board):
  s = square - 1
  if 'O' in board[s]:
    return 'O'
  elif 'X' in board[s]:
    return 'X'

board = [ 0, 'X', 0, 'X', 'O', 'O', 0 , 0, 0]
print(read(3,board))