class Solution:
  def generate(self, numRows: int) -> list[list[int]]:
    triangle = [] 

    for i in range(numRows):
      row = []
      for j in range(i+1):
        if (j == 0) or (j == i):
          row.append(1)
        else:
          value = triangle[i-1][j-1] + triangle[i-1][j]
          row.append(value)
      triangle.append(row)
          
    return triangle

sol = Solution()

print(sol.generate(numRows = 7)) #[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


        