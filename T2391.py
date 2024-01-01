class Solution:
  def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
    total = 0 
    i_M, i_P, i_G = 0, 0, 0 
    for i in range(len(garbage)-1,-1,-1):
      if i_M == 0 and "M" in garbage[i]: i_M = i
      if i_P == 0 and "P" in garbage[i]: i_P = i
      if i_G == 0 and "G" in garbage[i]: i_G = i
      total += len(garbage[i])
    total += sum(travel[:i_M]) + sum(travel[:i_P]) + sum(travel[:i_G])
    return total

sol=Solution()

print(sol.garbageCollection(garbage = ["G","P","GP","GG"], travel = [2,4,3])) # 21

print(sol.garbageCollection(garbage = ["MMM","PGM","GP"], travel = [3,10])) # 37

