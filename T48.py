class Solution:
  def rotate(self, matrix: list[list[int]]) -> list:
    line = zip(*matrix)
    for idx, row in enumerate(line):
      matrix[idx]=reversed(row)
     

    

          
    
sol=Solution()

print(sol.rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]])) #[[[7,4,1],[8,5,2],[9,6,3]]

