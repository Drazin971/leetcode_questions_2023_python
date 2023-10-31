class Solution:
  def integerBreak(self, n: int) -> int:
    dp = [0 for i in range(n+1)]
    dp[1] = 1
    for i in range(2, n+1):
      dp[i] = float("-inf")
      for j in range(1, i):
        dp[i] = max(dp[i], j * (i-j), j * dp[i - j])
    
      

    return dp[n]
    

sol = Solution()

print(sol.integerBreak(n = 10))  # 36