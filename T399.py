from collections import defaultdict

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
      graph = defaultdict(list)
      divs = {}
      res = []
      
      for i in range(len(equations)):
        u,v = equations[i]
        graph[u].append(v)
        graph[v].append(u)
        divs[(u,v)] = values[i]
        divs[(v,u)] = 1/values[i]
        
      def dfs(node,target, visited):
        if node in visited:
          return(float('inf'))
        if node == target:
          return 1
        visited.add(node)
        res=float('inf')
        for nn in graph[node]:
          res = min (res, dfs(nn, target, visited) * divs[(node, nn)])

        return res
            
      
      for query in queries:
        u, v = query
        if u not in graph or v not in graph:
          res.append(-1)
        else:
          c=dfs(u,v,set())
          res.append(-1) if c == float("inf") else res.append(c)
      return res
  
sol = Solution()

r=sol.calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]) #[6.0, 0.5, -1.0, 1.0, -1.0 ]

print(r)

r=sol.calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]) #[3.75000,0.40000,5.00000,0.20000]

print(r)

r=sol.calcEquation(equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]) #[0.50000,2.00000,-1.00000,-1.00000]

print(r)







