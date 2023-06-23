class Solution:
  def maxProfit(self, prices: list[int], fee: int) -> int:
    sell = 0
    buy = float('-inf')
    for i in range(len(prices)):
      buy = max(buy,sell - prices[i])
      sell = max(sell, prices[i] - fee + buy)
    return(sell)

    

          
    
sol=Solution()

print(sol.maxProfit(prices = [1,3,2,8,4,9], fee = 2)) #8
