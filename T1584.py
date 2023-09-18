class Solution:
  def minCostConnectPoints(self, points: list[list[int]]) -> int:

    def minDist(a, b):
      x1, y1 = a
      x2, y2 = b
      return abs(x1 - x2) + abs(y1 - y2)


    pass
    
sol = Solution()

print(sol.minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]]))