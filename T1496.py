class Solution:
  def isPathCrossing(self, path: str) -> bool:
    visited = [(0,0)]
    x, y = 0, 0 

    for l in path:
      if l == "N":
        y += 1
      if l == "S":
        y -= 1
      if l == "E":
        x += 1
      if l == "W":
        x -= 1
      for item in visited:
        if x == item[0] and y == item[1]: 
          return True
      visited.append((x,y))
    return False




sol=Solution()

print(sol.isPathCrossing("NESWW"))
