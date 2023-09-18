class Solution:
  def minPathSum(self, grid: list[list[int]]) -> int:
    r = len(grid)
    c = len(grid[0])

    for i in range(1,r):
      grid[i][0] += grid[i-1][0]

    for j in range(1,c):
      grid[0][j] += grid[0][j-1]

    for row in range(1,r):
      for column in range (1,c):
        grid[row][column] += min(grid[row-1][column], grid[row][column-1])
          
    return grid[r-1][c-1]
    

sol=Solution()

print(sol.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]])) #7

print(sol.minPathSum(grid = [[1,2,3],[4,5,6]])) #12



