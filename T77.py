class Solution:
  def combine(self, n: int, k: int) -> list[list[int]]:
    res = []
    
    def btrack(curr: list[int],start: int) -> list:
      if len(curr)==k:
        res.append(curr.copy())
        return
      for i in range(start,n+1):
        if i not in curr:
          curr.append(i)
          btrack(curr,i+1)
          curr.pop()
      
    btrack([],1)
    
    return res

sol = Solution()

r=sol.combine(n = 4, k = 2) #Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

print(r)

r=sol.combine(n = 1, k = 1) #[[1]]

print(r)