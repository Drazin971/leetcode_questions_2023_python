class Solution:
  def gameOfLife(self, board: list[list[int]]) -> None:
    rows = len(board)
    columns = len(board[0])
    temp_board = [[0] * columns for _ in range(rows)]
  
    def get_alive_number(x,y) -> int:
     nei =0
     nonlocal board, rows, columns
     for dx in [-1,0,1]:
       for dy in [-1,0,1]:
         if dx== 0 and dy==0:
           continue
         nx = x + dx
         ny = y + dy
         #print(nx, ny) 
         if 0<=nx<rows and 0<=ny<columns:
           nei += board[nx][ny]
          
     return nei  
    
    for i in range(rows):
      for j in range(columns):
        temp_board[i][j]=get_alive_number(i,j)      

    for i in range(rows):
      for j in range(columns):
        if board[i][j]==1:
          if temp_board[i][j]<2 or temp_board[i][j] >3:
            board[i][j]=0
        elif temp_board[i][j]==3:
           board[i][j]=1