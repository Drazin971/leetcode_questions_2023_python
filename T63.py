class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

    r = len(obstacleGrid)
    c = len(obstacleGrid[0])

    memo = [0] * c
    memo[c-1] = 1

    for i in reversed(range(r)):
      for j in reversed(range(c)):
        if obstacleGrid[i][j]: 
          memo[j] = 0
        elif j + 1 < c:
          memo[j] += memo[j+1]
        

    return memo[0]
  

sol = Solution()

print(sol.uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]])) #2

print(sol.uniquePathsWithObstacles(obstacleGrid = [[0,1],[0,0]])) #1

