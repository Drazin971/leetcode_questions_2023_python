class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
      totalTime = 0
      for index, value in enumerate(informTime):
        time=0
        if value == 0:
          i=index
          while manager[i]!=-1:
            i = manager[i]
            time += informTime[i]
          
          if time>totalTime:
            totalTime = time
         
      return(totalTime)
            
        
      
        


sol = Solution()

print(sol.numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]))