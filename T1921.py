class Solution:
  def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
    n = len(dist)
    for i in range(n):
      print(dist)
      dist = dist - speed

sol=Solution()

print(sol.eliminateMaximum(dist = [1,1,2,3], speed = [1,1,1,1])) #4