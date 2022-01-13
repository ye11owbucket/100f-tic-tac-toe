def read(square,board):
  square -= 1
  if "O" in square[board]:
    return "O"
  elif "X" in square[board]:
    return "X"
  else:
   return None
board = [ 0, 'X', 0, 'X', 'O', 'O', 0 , 0, 0]
print(read(3,board))