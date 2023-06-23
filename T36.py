class Solution:
  def checkValidBox(self, board: list[list[str]], x, y) -> bool:
    curr_board = []
    for c in range(3):
      for r in range(3):
        if board[c+x*3][r+y*3].isnumeric()==True:
          if board[c+x*3][r+y*3] not in curr_board:
            curr_board.append(board[c+x*3][r+y*3])
            #print(curr_board)
          else: return False
    return True
  
  def isValidSudoku(self, board: list[list[str]]) -> bool:
   for box in range(9):
    x,y = (divmod(box,3))
    if self.checkValidBox(board, x, y) == False:
      return False
    
    curr_row=[]
    curr_column=[]
    for c in range(9):
      curr_row.clear()
      curr_column.clear()
      for r in range(9):
        if board[r][c].isnumeric()==True:
          if board[r][c] not in curr_row:
            curr_row.append(board[r][c])
          else: return False
        if board[c][r].isnumeric()==True:
          if board[c][r] not in curr_column:
            curr_column.append(board[c][r])
          else: return False
        
     
    for box in range(9):
      x,y = (divmod(box,3))
      #print(x+1,y+1)
      if self.checkValidBox(board, x, y) == False:
        return False

    return True
            
          
         
          
    
sol=Solution()

print(sol.isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])) #true

print(sol.isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])) #false

print(sol.isValidSudoku(board = 
[["1","2","3",".","7",".",".",".","."]
,["6","5","4","1","9","5",".",".","."]
,["7","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])) #false

