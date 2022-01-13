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
  blankBoard = [1,2,3,4,5,6,7,8,9]
  for square in range(1,9):
        if (board[square] == 'O' or board[square] == 'X'):
            blankBoard = blankBoard.replace(str(square), board[square])
        else:
            blankBoard = blankBoard.replace(str(square), ' ')
  return blankBoard



def write(square,board,player):
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
  
  return None

def mainRead():
  board = [ 0, 'X', 0, 'X', 'O', 'O', 0 , 0, 0]
  assert read(3,board) == None
  assert read(2,board) == 'X'
  assert read(5,board) == 'O'

def mainWrite():
  board = [ 0,0,0,0,0,0,0,0,0,0]
  assert write(1,board,'X') == [ 'X',0,0,0,0,0,0,0,0,0]
  assert write(5,board,'O') == [ 'X',0,0,0,'O',0,0,0,0,0]
  #next command should not do anything because square #5 is already occupied by an 'O'
  assert write(5,board,'X') == [ 'X',0,0,0,'O',0,0,0,0,0]
 
  
  
if __name__ == "__main__" :
  mainRead()
  mainWrite()
