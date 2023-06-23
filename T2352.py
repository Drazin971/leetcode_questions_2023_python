class Solution:
  def equalPairs(self, grid: list[list[int]]) -> int:
    total=0
    new_grid = [list(col) for col in zip(*grid)]
    for item in grid:
      total+=new_grid.count(item)
 
    return total
      
    
    

 
    
  

sol=Solution()

print(sol.equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]])) #1
print(sol.equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])) #3
print(sol.equalPairs(grid = [[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]])) #3