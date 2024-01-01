class Solution:
  def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
      max_area = 0
      points.sort(key = lambda x: x[0])
      for i in range(1,len(points)):
          max_area = max(max_area, points[i][0] - points[i-1][0])
      return max_area

sol=Solution()

print(sol.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))