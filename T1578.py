class Solution:
  def minCost(self, colors: str, neededTime: list[int]) -> int:
    total = 0
    l,r = 0, 0 

    while r < len(colors):
      ctotal, cmax = 0, 0
      while r < len(colors) and colors[l] == colors[r]:
        ctotal += neededTime[r]
        cmax = max(cmax, neededTime[r])
        r += 1
      total += ctotal - cmax
      l = r

    return total



sol=Solution()

print(sol.minCost(colors = "abaac", neededTime = [1,2,3,4,5])) # 3