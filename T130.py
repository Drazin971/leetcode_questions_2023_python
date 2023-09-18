class Solution:
 def solve(self, board: list[list[str]]) -> None:
   q=[]
   visited = set()

   def is_valid(board, r, c):
     return r>0 and c>0 and r<len(board)-1 and c<len(board[0])-1
   
   def get_neighbours(board, r, c):
     neighbours = [(r+1,c), (r-1,c), (r, c+1), (r, c-1)]
     return [(row,column) for row, column in neighbours if is_valid(board, row, column) and board[row][column]=="O"]
     
   def bfs(board,r,c):
     q.append((r,c))
     while q:
       row,column = q.pop()
       visited.add((row,column))
       
       for r,c in get_neighbours(board, row, column):
         if (r,c) not in visited:
           q.append((r,c))
       
     pass

   for r in range(len(board)):
    for c in range(len(board[0])):
      if board[r][c]=="O":
        if (r==0 or r==len(board)-1 or c==0 or c==len(board[0])-1):
          bfs(board, r,c)

   #print(visited)
     
   for r in range(len(board)):
     for c in range(len(board[0])):
       if (r,c) in visited:
         board[r][c]=="O"
       else:
         board[r][c] ="X"
   
   return None
   
  
sol = Solution()

b= [["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]

sol.solve(b)

for row in b:
  print(row)
