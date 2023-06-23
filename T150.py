class Solution:
  def hIndex(self, citations: list[int]) -> int:
    current_max=0
    for i in range(1,len(citations)+1):
      hsum=sum(1 for item in citations if item>=i) 
      if hsum>=i:
       current_max=max(current_max,i)
      
    return current_max
      
      

sol = Solution()

print(sol.hIndex(citations = [1]))