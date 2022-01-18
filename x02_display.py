#!python3

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

def main():
  board = [ 'O' , 0 , 0 , 'X' , 'O' , 0 , 0 , 0 , 'X' ] 
  assert displayString(board) == "- - X\nX O -\nO - -"
  board = [ 0 , 'O' , 'X' , 'O' , 'O' , 0 , 'X' , 0 , 'X' ] 
  assert displayString(board) == "X - X\nO O -\n- O X"

if __name__ == "__main__":
  main()

  """
  function should create a string that can be displayed using a print command
  this function should have no actual print commands in it
  
  input:
  list board: the game board data:
  7 8 9
  4 5 6
  1 2 3
  
  eg 
  board = [ 'O' , 0 , 0 , 'X' , 'O' , 0 , 0 , 0 , 'X' ] 
  should display:
  - - X
  X O -
  O - -
  
  return value
  str the gameboard
  """