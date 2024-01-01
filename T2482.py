import numpy as np

class Solution:
  def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
    ar = np.array(grid)
    m, n=len(grid), len(grid[0])
    cols=np.sum(ar, axis=0)
    rows=np.sum(ar, axis=1)
    rows=rows.reshape(m, 1)      
    ar=2*(rows+cols)-(m+n)
    return ar
    
    

sol=Solution()

print(sol.onesMinusZeros(grid = [[0,1,1],[1,0,1],[0,0,1]])) # 13