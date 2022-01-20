def replayString(board):
  kill = '-'
  if kill in board:
    for i in board:
      x = board.index(kill)
      board.pop(x)
      board.insert(x,0)
      if kill not in board:
        break
  return board

