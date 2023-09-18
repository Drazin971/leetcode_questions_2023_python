class Solution:
  def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    i=0
    while matrix[i][-1]<target and i<len(matrix)-1:
      i+=1
      
    return True if target in matrix[i] else False

sol=Solution()

r=sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3) #True

print(r)