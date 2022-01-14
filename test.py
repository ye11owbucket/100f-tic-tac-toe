



def write(square,board,player):
  if 0 in board[square]:
    x = board.index(square)
    board.pop(x)
    board.insert(x,player)
    return board
  elif 'O' in board[square]:
    return (board , "spot occupied")
  elif 'X' in board[square]:
    return (board , "spot occupied")
  if 0 in board[square]:
    x = board.index(square)
    board.pop(x)
    board.insert(x,player)
    return board

board = [ 0, 'X', 0, 'X', 'O', 'O', 0 , 0, 0]
print(write(3,board,'O'))