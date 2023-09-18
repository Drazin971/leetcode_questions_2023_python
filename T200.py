class Solution:
 def numIslands(self, grid: list[list[str]]) -> int:
   visited = set()
   queue = []
   sol=0

   if not grid: return 0

   def is_valid(grid,row,col) -> bool:
     return row>=0 and col>=0 and row<len(grid) and col<len(grid[0])
     
   def get_neighbours(grid, row, col) -> list:
     neighbours = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
     return [(row, column) for row,column in neighbours if is_valid(grid,row, column) and grid[row][column]=="1"]

   def bfs(grid, r, c):
      queue.append((r, c))
      while len(queue) > 0:
        current_row, current_col = queue.pop()
        if (current_row, current_col) not in visited:
          visited.add((current_row, current_col))
          for neighbor_row, neighbor_col in get_neighbours(grid, current_row, current_col):
            if (neighbor_row, neighbor_col) not in visited:
              queue.append((neighbor_row, neighbor_col))
   

   for i in range(len(grid)):
     for j in range(len(grid[0])):
      if grid[i][j]=="1" and ((i,j) not in visited):
        bfs(grid,i,j)
        sol+=1
        
          
    
   return sol