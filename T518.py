class Solution:
  def change(self, amount: int, coins: list[int]) -> int:

    memo = {}

    def dfs(i, a):
      if a == amount:
        return 1
      if a > amount:
        return 0
      if i == len(coins):
        return 0      
      if (i,a) in memo: 
        return memo[(i,a)]
        
      memo[(i,a)] = dfs(i, a + coins[i]) + dfs(i+1,a)
      return memo[(i,a)]
      


    return dfs(0,0)


sol = Solution()

print(sol.change(amount = 5, coins = [1,2,5])) #4

print(sol.change(amount = 3, coins = [2])) #0

print(sol.change(amount = 10, coins = [10])) #1