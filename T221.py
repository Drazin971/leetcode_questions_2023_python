class Solution:
  def maximalSquare(self, matrix: list[list[str]]) -> int:

    rows = len(matrix)
    columns = len(matrix[0])
    sol = 0

    memo = [[0] * (columns + 1) for _ in range(rows+1)]
     
    for i in range(rows - 1, -1, -1):
      for j in range(columns -1, -1, -1):
        if matrix[i][j] == "1":
          r = memo[i][j+1] 
          d = memo[i+1][j] 
          diag = memo[i+1][j+1]
          memo[i][j] = 1 + min(r,d,diag)
          if memo[i][j] > sol: sol = memo[i][j]
          
    return sol**2



sol = Solution()

print(sol.maximalSquare(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])) #4

print(sol.maximalSquare(matrix = [["0","1"],["1","0"]])) #1