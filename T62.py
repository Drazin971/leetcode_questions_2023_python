class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    if (m<2) or (n<2): return 1
    paths = [[1] * n for _ in range(m)]

    for i in range(1,m):
      for j in range(1, n):
        paths[i][j]= paths[i-1][j]+paths[i][j-1]

    return paths[m-1][n-1]
      

sol = Solution()

print(sol.uniquePaths(m = 3, n = 7)) #28

print(sol.uniquePaths(m = 3, n = 2)) #3
        