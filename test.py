def displayString(board):
  kill = 0
  if kill in board:
    for i in board:
      x = board.index(kill)
      board.pop(x)
      board.insert(x,'-')
      if kill not in board:
        break
  board.insert(1, " ")
  board.insert(3, " ")
  board.insert(5, "\n")
  board.insert(7, " ")
  board.insert(9, " ")
  board.insert(11, "\n")
  board.insert(13, " ")
  board.insert(15, " ")
  fboard = ''.join(board)
  return fboard

def whoWins(board):
  count = 0
  if 'X' == board[0]:
    if 'X' == board[1]:
      if 'X' == board[2]:
        return 'X'
  if 'X' == board[0]:
    if 'X' == board[4]:
      if 'X' == board[8]:
        return 'X'
  if 'X' == board[0]:
    if 'X' == board[3]:
      if 'X' == board[6]:
        return 'X'
  if 'X' == board[3]:
    if 'X' == board[4]:
      if 'X' == board[5]:
        return 'X'
  if 'X' == board[6]:
    if 'X' == board[7]:
      if 'X' == board[8]:
        return 'X'
  if 'X' == board[1]:
    if 'X' == board[4]:
      if 'X' == board[7]:
        return 'X'
  if 'X' == board[2]:
    if 'X' == board[4]:
      if 'X' == board[6]:
        return 'X'
  else:
    return "tragic"
board = [ 'X',0,0,0,'X',0,'O','O','X']
print(whoWins(board))