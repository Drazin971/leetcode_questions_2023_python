class Solution:
  def numberOfMatches(self, n: int) -> int:
    if n == 1:
      return 0
    return self.numberOfMatches(n // 2) + n // 2 if n % 2 == 0 else (n -1) // 2

sol=Solution()

print(sol.numberOfMatches(n = 14)) # 13