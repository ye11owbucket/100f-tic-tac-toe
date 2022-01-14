def read(square,board):
  if 'O' in board[square]:
    return 'O'
  if 'X' in board[square]:
    return 'X'
  else:
    return None

def mainRead():
  board = [ 0, 'X', 0, 'X', 'O', 'O', 0 , 0, 0]
  assert read(2,board) == None
  assert read(1,board) == 'X'
  assert read(4,board) == 'O'


if __name__ == "__main__" :
  mainRead()