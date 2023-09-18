class Solution:
  def coinChange(self, coins: list[int], amount: int) -> int:

    dp = [amount*2] * (amount + 1)
    dp[0] = 0

    for i in range(1,amount+1):
      for coin in coins:
        if coin <= i:
          dp[i] = min(dp[i], 1 + dp[i - coin] )
          
    #print(dp)
    return dp[amount] if dp[amount] != amount * 2 or amount == 0 else -1
      

sol=Solution()

print(sol.coinChange(coins = [1,2,5], amount = 11)) #3

print(sol.coinChange(coins = [2], amount = 3)) #-1

print(sol.coinChange(coins = [1], amount = 0)) #0
