class Solution:
    def maxProfit(self, prices: list[int]) -> int:
      maximum_price = 0
      mininum_value = float('inf')
     
      for i in range(len(prices)):
        mininum_value = min(mininum_value,prices[i])
        if prices[i]>mininum_value:
          maximum_price = max(maximum_price, prices[i]-mininum_value)

      return maximum_price

sol = Solution()

print(sol.maxProfit(prices = [7,1,5,3,6,4]))