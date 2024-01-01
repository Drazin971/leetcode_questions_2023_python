class Solution:
  def largestSubmatrix(self, matrix: list[list[int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(1,rows):
      for j in range(cols):
        if matrix[i][j] == 1:
          matrix[i][j] = matrix[i-1][j] + 1

    res = 0

    for i in range(rows):
      matrix[i].sort()
      for j in range(cols):
        w = matrix[i][j]
        b = cols - j 
        res = max(res, w * b)

    return res

sol=Solution()

print(sol.largestSubmatrix(matrix = [[0,0,1],[1,1,1],[1,0,1]])) # 4