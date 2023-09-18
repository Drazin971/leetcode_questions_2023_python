class Solution:
  def lengthOfLIS(self, nums: list[int]) -> int:

    dp = [1] * len(nums)

    for i in range(len(nums)-1,-1,-1):
      for j in range(i+1, len(nums)):
        if nums[i] < nums [j]:
          dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
      
      
    
      

sol=Solution()

print(sol.lengthOfLIS(nums = [10,9,2,5,3,7,101,18])) #4

print(sol.lengthOfLIS(nums = [0,1,0,3,2,3])) #4

print(sol.lengthOfLIS(nums = [7,7,7,7,7,7,7])) #1