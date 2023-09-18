from collections import defaultdict

class Solution:
  def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    adj = defaultdict(list)
    res = []
    visited = {}
    
    for course, pre in prerequisites:
      adj[pre].append(course)

    def dfs(i: int):
      if i in visited:
        return visited[i]
      visited[i]=True
      for outgoing in adj[i]:
        if dfs(outgoing): return True
      visited[i]=False
      res.append(i)
      return False
    
    for i in range(numCourses):
       if dfs(i) == True: return []

    return list(reversed(res))
                     
sol = Solution()

r=sol.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]) #[0,2,1,3]

print(r)

r=sol.findOrder(numCourses = 2, prerequisites = [[1,0],[0,1]]) #[]

print(r)