class Solution:
  def maxProfit(self, prices: list[int]) -> int:
    total = 0 
    for i in range(len(prices)-1):
      if prices[i+1]>prices[i]:
        total+=prices[i+1]-prices[i]
      
    return total
     
      

sol = Solution()

print(sol.maxProfit(prices = [7,1,5,3,6,4]))