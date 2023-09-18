class Solution:
  def trailingZeroes(self, n: int) -> int:
    
    def silnia(i: int):
      if i==1: return 1
      return i*silnia(i-1)
    
    for i in range(1,31):
      print(silnia(i))
    

sol=Solution()

print(sol.trailingZeroes(n = 30)) #True
