class Solution:
  def totalMoney(self, n: int) -> int:
    if n < 6:
      return (2* n + 5) * n / 2
    return self.totalMoney((2* n + 5) * n / 2) 

sol=Solution()

print(sol.totalMoney(n = 20)) # 96