class Solution:
  def findContentChildren(self, g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()
    happy_kids = 0
    i = 0
    while i < len(s) and happy_kids < len(g) :
      if s[i] >= g[happy_kids]:
        happy_kids += 1
      i += 1
    return happy_kids



sol=Solution()

print(sol.findContentChildren(g = [1,2,3], s = [1,1])) # 1

print(sol.findContentChildren(g = [1,2], s = [1,2,3])) # 2