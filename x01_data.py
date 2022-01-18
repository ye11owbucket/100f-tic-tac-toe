#!python3

""" 
Create a reliable method for storing and retrieving data for the game.
"""
"""
This will do a lookup to find out what is in a particular square
  inputs: 
  list board : list of the squares in the board
    7 | 8 | 9
    4 | 5 | 6
    1 | 2 | 3
  int square: the square you are checking for an X or an O
  
  return:
  the str value corresponding to the content of the square being checked
  None if the square is empty
  """
def read(square,board):
  if 'O' == board[square]:
    return 'O'
  elif 'X' == board[square]:
    return 'X'
  else:
    return None

def write(square,board,player):
  if 0 == board[square]:
    board.pop(square)
    board.insert(square,player)
    return board
  elif 'O' == board[square]:
    return board
  elif 'X' == board[square]:
    return board

def mainRead():
  board = [ 0, 'X', 0, 'X', 'O', 'O', 0 , 0, 0]
  assert read(2,board) == None
  assert read(1,board) == 'X'
  assert read(4,board) == 'O'

def mainWrite():
  board = [ 0,0,0,0,0,0,0,0,0,0]
  assert write(0,board,'X') == [ 'X',0,0,0,0,0,0,0,0,0]
  assert write(4,board,'O') == [ 'X',0,0,0,'O',0,0,0,0,0]
  #next command should not do anything because square #5 is already occupied by an 'O'
  assert write(4,board,'X') == [ 'X',0,0,0,'O',0,0,0,0,0]
 
  
  
if __name__ == "__main__" :
  mainRead()
  mainWrite()


  """
  inputs:
  int square : the square you are checking for an X or an O
  list board : the complete game board stored as a list
  str player : either an 'X' or an 'O' 
  
  return:
  the updated gameboard with the new data
  
  The function should update the contents of the gameboard if the square is
  empty.  If the square is not empty, it should not change the gameboard and
  should return the original, unchanged gameboard data
  """