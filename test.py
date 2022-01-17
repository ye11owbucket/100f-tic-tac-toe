def write(square,board,player):
  square -= square
  while True:
    if 0 == board[square]:
      board.pop(square)
      board.insert(square,player)
      return board
    elif 'O' == board[square]:
      return board
    elif 'X' == board[square]:
      return board
    elif 0 not in board:
      return False
  
def mainWrite():
  board = [ 0,0,0,0,0,0,0,0,0,0]
  assert write(0,board,'X') == [ 'X',0,0,0,0,0,0,0,0,0]
  assert write(4,board,'O') == [ 'X',0,0,0,'O',0,0,0,0,0]
  #next command should not do anything because square #5 is already occupied by an 'O'
  assert write(4,board,'X') == [ 'X',0,0,0,'O',0,0,0,0,0]
 

board = [ 0,0,0,0,0,0,0,0,0,0]
print(write(0,board,'X'))
print(write(4,board,'O'))
print(write(4,board,'X'))