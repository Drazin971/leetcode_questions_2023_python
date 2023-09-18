class Solution:
  def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
    directions = [[1,2],[-1,2],[2,1],[-2,1],
                  [1,-2],[-1,-2],[2,-1],[-2,-1]]
    
    dp={}
    
    def is_valid(r,c):
      return 0 <= r < n and 0 <= c < n

    def dfs(row: int, column: int, move: int):
      if (row, column, move) in dp:
        return dp[(row, column, move)]
        
      if move == k:
        return 1

      ans = 0
      
      for direction in directions:
        r, c = direction
        r=r+row
        c=c+column
        if is_valid(r,c):
          ans += 0.125 * dfs(r,c, move + 1)

      dp[(row, column, move)] = ans

      return ans
          
    return dfs(row, column, 0)

sol = Solution()

r=sol.knightProbability(n = 3, k = 2, row = 0, column = 0) #0.06250

print(r)

r=sol.knightProbability(n = 1, k = 0, row = 0, column = 0) #1

print(r)

r=sol.knightProbability(n = 8, k = 30, row = 6, column = 4) #1

print(r)
