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
  board.insert(3, "\n")
  board.insert(7, "\n")
  fboard = ''.join(board)
  return fboard

def main():
  board = [ 'O' , 0 , 0 , 'X' , 'O' , 0 , 0 , 0 , 'X' ] 
  assert displayString(board) == "- - X\nX O -\nO - -"
  board = [ 0 , 'O' , 'X' , 'O' , 'O' , 0 , 'X' , 0 , 'X' ] 
  assert displayString(board) == "X - X\nO O -\n- O X"

if __name__ == "__main__":
  main()

