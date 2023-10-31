class Solution:
  def minCostClimbingStairs(self, cost: list[int]) -> int:

    dp = [0 * len(cost)]

    for i in range(len(cost)-2,-1,-1):
      dp[i] = min(dp[i+1], dp[i] + cost[i])

    print(dp)

    return dp[0]

sol = Solution()

print(sol.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))  # 6

    