class Solution:
  def jump(self, nums: list[int]) -> int:
    dp = [0] * len(nums) 

    for i in range(len(nums) - 2 , -1, -1):
      res = float('inf')
      for j in range(i + 1, min(i + nums[i] + 1 , len(nums))):
        res = min(res, dp[j])
      dp[i] = 1 + res

    #print(dp)
    
    return dp[0]
        
        
   


sol = Solution()

print(sol.jump(nums = [2,3,1,1,4]))

