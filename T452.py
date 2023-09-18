class Solution:
  def findMinArrowShots(self, points: list[list[int]]) -> int:
    points = sorted(points)
    merged = []
    
    for interval in points:
      if not merged or interval[0]>merged[-1][1]:
        merged.append(interval)
      else:
        merged[-1][0]=max(merged[-1][0],interval[0])
        merged[-1][1]=min(merged[-1][1],interval[1])
    #print(merged)
    return len(merged)
      
  
  
 

sol=Solution()

print(sol.findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]])) #2

print(sol.findMinArrowShots(points = [[1,2],[3,4],[5,6],[7,8]])) #4

print(sol.findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]])) #2