class Solution:
  def setZeroes(self, matrix: list[list[int]]) -> None:
   n = len(matrix) #rows
   m = len(matrix[0]) #columns
   columns_to_zero = set()
   rows_to_zero = set()
    
   for i in range(n):
    for j in range(m):
      if matrix[i][j]==0:
        rows_to_zero.add(i)
        columns_to_zero.add(j)

   #print(rows_to_zero) 
   #print(columns_to_zero)
    
   for row in rows_to_zero:
     matrix[row] = [0 for _ in range(m)]
    
   for column in columns_to_zero:
    for a in range(n):
     matrix[a][column] = 0

  
   #print(matrix)
          
    
sol=Solution()

print(sol.setZeroes(matrix = [[1,1,1],[1,0,1],[1,1,1]])) #[[1,0,1],[0,0,0],[1,0,1]]

print(sol.setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]])) #[[0,0,0,0],[0,4,5,0],[0,3,1,0]]








