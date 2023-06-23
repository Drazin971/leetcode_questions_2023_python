class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
      n=len(grid)
      visited=[[0]*n for _ in range(n)]
      n-=1
      if grid[0][0]==1:
          return -1
      queue=[(0,0,1)]
      visited[0][0]=1
      print(queue)
      while queue:
        x,y,d = queue.pop(0)

        if (x==n) and (y==n):
          return d
        
        for i in range(-1,2):
          for j in range(-1,2):
            if (i+x>=0) and (i+x<=n) and (j+y>=0) and (j+y<=n):
             if (visited[i+x][j+y] ==0) and grid[i+x][j+y]==0:
              print(i+x,j+y)
              queue.append((i+x, j+y, d+1))
              visited[i+x][j+y]=1
              
      return -1 


sol = Solution()

print(sol.shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,1]]))