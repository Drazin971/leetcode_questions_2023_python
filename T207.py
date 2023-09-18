import collections

class Solution:
  def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
    adj = collections.defaultdict(list)
    visited = {}

    for curse, prereq in prerequisites:
      adj[prereq].append(curse) 
   
    def cycle(i: int, t: dict, visited: dict): 
      t[i]=True
      visited[i] = True
      for j in adj[i]:
        if j not in visited and cycle(j, t, visited):
          return True
        elif j in t:
          return True
      t.pop(i)
      return False

    for i in range(numCourses):
      t ={}
      if i not in visited and cycle(i, t, visited):
        return False
    
    return True
  
sol = Solution()

r=sol.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]) #false

print(r)