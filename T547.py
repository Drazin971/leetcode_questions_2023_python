class Solution:
  def findCircleNum(self, isConnected: list[list[int]]) -> int:
    n = len(isConnected) 
    result = 0

    def dfs(i):
      for j in range(n):
        if isConnected[i][j]==1:
          isConnected[i][j]=2
          dfs(j)
      
    for i in range(n):
      if isConnected[i][i]==1:
        result+=1
        dfs(i)
      

    return result
        
      
        


sol = Solution()

#print(sol.findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]]))

print(sol.findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]]))