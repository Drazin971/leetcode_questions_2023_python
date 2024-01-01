class Solution:
  def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
    dist = 0

    for i in range(len(points)-1):
      #min_distance = min(abs(points[i][0] - points[i+1][0]), abs(points[i][1] - points[i+1][1]))
      max_distace = max(abs(points[i][0] - points[i+1][0]), abs(points[i][1] - points[i+1][1]))
      dist += max_distace
      
    return max_distace
    

sol=Solution()

print(sol.minTimeToVisitAllPoints(points = [[1,1],[3,4],[-1,0]])) # 7