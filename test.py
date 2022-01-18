def whoWins(board):
  count = 0
  if 'X' == board[0]:
    if 'X' == board[1]:
      if 'X' == board[2]:
        return 'X'
  else:
    return None