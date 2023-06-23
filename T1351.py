class Solution:
  def countNegatives(self, grid: list[list[int]]) -> int:
    m=len(grid)
    n=len(grid[0])
    negative_numbers=0
    for i in range(m):
      for j in range(n):
        if grid[i][j]<0:
          negative_numbers+=n-j
          break
    return negative_numbers
              
            


sol = Solution()

print(sol.countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))