class Solution:
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    ans = [0] * (len(nums))  
    if nums.count(0)>1:
     return ans
    elif nums.count(0)==1:
      nums[nums.index(0)] = i*=i
    for i in range(len(nums)):
      ans[i] = sum(nums) / nums[i]
    return ans    

sol = Solution()


print(sol.productExceptSelf(nums = [-1,1,0,-3,3]))


