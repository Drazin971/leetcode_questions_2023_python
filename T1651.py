from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
      graph = defaultdict(set)
      max_rank = 0
      
      for c1, c2 in roads:
        graph[c1].add(c2)
        graph[c2].add(c1)

      for c1 in range(n):
        for c2 in range(n):
          if c1 == c2: continue
          curr_rank = graph[c1].values() + graph[c2].values
          if c2 in graph[c1]:
            curr_rank -= 1
          max_rank = max(max_rank, curr_rank)
          
      return max_rank
        



sol = Solution()

print(sol.updateMatrix(n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]))

print(sol.updateMatrix(n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]))