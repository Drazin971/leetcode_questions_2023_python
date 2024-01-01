import numpy as np
class Solution:
  def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
    return np.array(matrix).transpose()
sol=Solution()

print(sol.transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]])) # 13