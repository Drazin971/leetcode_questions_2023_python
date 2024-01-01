from collections import defaultdict

class Solution:
  def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
    adj = defaultdict(set)

    for r in routes:
      for i in r:
        if i != adj[i]:
          adj[i].add(r[i])

    print(adj)

sol=Solution()

print(sol.adjacentPairs(routes = [[1,2,7],[3,6,7]], source = 1, target = 6)) #4 