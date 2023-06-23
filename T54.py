class Solution:
  def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
    n_max=len(matrix)-1
    m_max=len(matrix[0])-1
    matrix_len = len(matrix) * len(matrix[0])
    x,y=0,0
    n_min, m_min=1,0
    snake_matrix = []
    dir_x, dir_y = 1, 0

    if m_max==0:
      return list(matrix[i][0] for i in range(len(matrix)))
    
    while len(snake_matrix)<matrix_len:
      #print(n_max, m_max)
      snake_matrix.append(matrix[y][x])
      x += dir_x
      y += dir_y
      if x==m_max and dir_x==1:
        dir_x, dir_y = 0,1
        m_max -= 1
      elif x==m_min and dir_x==-1:
        dir_x, dir_y = 0,-1
        m_min += 1
      elif y==n_max and dir_y==1:
        dir_x, dir_y=-1,0
        n_max -= 1
      elif y==n_min and dir_y==-1:
        dir_x, dir_y=1,0
        n_min += 1
      
     
    return snake_matrix

          
    
sol=Solution()

print(sol.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]])) #[1,2,3,6,9,8,7,4,5]

print(sol.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]])) #[1,2,3,4,8,12,11,10,9,5,6,7]

print(sol.spiralOrder(matrix = [[3],[2],[4]])) #[3,2]





