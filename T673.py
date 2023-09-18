class Solution:
  def findNumberOfLIS(self, nums: list[int]) -> int:
    dp = {}
    sol_LIS, sol = 0, 0

    for i in range(len(nums) - 1, -1, -1):
      max_LIS, max_count = 1, 1

      for j in range(i+1, len(nums)):
        if nums[j]>nums[i]:
          cur_LIS, cur_count = dp[j]
          if cur_LIS+1>max_LIS:
            max_LIS, max_count = 1 + cur_LIS, cur_count
          elif cur_LIS+1==max_LIS:
            max_count += cur_count

      dp[i]=[max_LIS, max_count]      

      if max_LIS+1>sol_LIS:
        sol_LIS, sol = 1 + max_LIS, max_count
      elif max_LIS+1==sol_LIS:
        sol += max_count

    return sol
      
        
    


sol = Solution()

r=sol.findNumberOfLIS(nums = [1,3,5,4,7]) #2

print(r)

r=sol.findNumberOfLIS(nums = [2,2,2,2,2]) #5

print(r)