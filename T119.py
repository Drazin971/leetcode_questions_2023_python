class Solution:
  def getRow(self, rowIndex: int) -> list[int]:
    if rowIndex == 0:
      return [1]
    current_row = [1] * (rowIndex + 1)
    prev_row =  [1] * (rowIndex + 1)

    for i in range(1, rowIndex + 1):
      prev_row = current_row.copy()
      for j in range(1,i):
        current_row[j] = prev_row[j-1] + prev_row[j]

    return current_row   

sol = Solution()

print(sol.getRow(rowIndex = 3))  # [1,3,3,1]