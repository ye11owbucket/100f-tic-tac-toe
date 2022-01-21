def displayString(board):
  kill = 0
  if kill in board:
    for i in board:
      x = board.index(kill)
      board.pop(x)
      board.insert(x,'-')
      if kill not in board:
        break
  board.insert(3, "\n")
  board.insert(7, "\n")
  board.pop()
  fboard = ''.join(board)
  return fboard

board = [ 0,0,0,0,0,0,0,0,0,0]
print(displayString(board))
