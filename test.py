def displayString(board):
  kill = 0
  print(board)
  if kill in board:
    print(board)
    for i in board:
      print(board)
      x = board.index(kill)
      board.pop(x)
      board.insert(x,'-')
      if kill not in board:
        break
  fboard = "\n".join(board)
  return fboard
board = [ 0 , 'O' , 'X' , 'O' , 'O' , 0 , 'X' , 0 , 'X' ] 
print(displayString(board))