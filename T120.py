class Solution:
  def minimumTotal(self, triangle: list[list[int]]) -> int:
      columns = len(triangle) - 1

      for i in range(columns,0,-1):
        for j in range(len(triangle[i-1])):

          triangle[i-1][j] += min(triangle[i][j],triangle[i][j+1])
    
      return triangle[0][0]

sol=Solution()

print(sol.minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]])) #11

print(sol.minimumTotal(triangle = [[-10]])) #-10
