class Solution:
  def validPartition(self, nums: list[int]) -> bool:
    dp = [False] * len(nums)
    dp[1] = True if nums[0] == nums[1] else False

    for i in range(2, len(nums)):
      #print(nums[i], dp)
      if nums[i] == nums[i-1]:
        dp[i] = dp[i-2] 
      if (nums[i] == nums[i-1] == nums[i-2]):
        dp[i] = dp[i-3] if (i > 2 and dp[i] == False) else True
      if (nums[i] == nums[i-1] + 1 == nums[i-2] + 2):
        dp[i] = dp[i-3] if (i > 2 and dp[i] == False) else True
          
    return dp[len(nums)-1]

sol = Solution()

#print(sol.validPartition(nums = [4,4,4,5,5,5])) #True

print(sol.validPartition(nums = [676575,676575,676575,533985,533985,40495,40495,40495,40495,40495,40495,40495,782020,782021,782022,782023,782024,782025,782026,782027,782028,782029,782030,782031,782032,782033,782034,782035,782036,782037,782038,782039,782040,378070,378070,378070,378071,378072,378073,378074,378075,378076,378077,378078,378079,378080,378081,378082,378083,378084,378085,378086,378087,378088,378089,378090,378091,378092,378093,129959,129959,129959,129959,129959,129959])) #False