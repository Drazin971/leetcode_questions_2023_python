class Solution:
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    ans = [1] * (len(nums))  
    l_product, r_product = 1, 1

    for i in range(len(nums)):
      ans[i] *= l_product
      l_product *= nums[i]
      
      ans[len(nums)-i-1] *= r_product
      r_product *= nums[len(nums)-i-1]

    return ans    

sol = Solution()


print(sol.productExceptSelf(nums = [-1,1,0,-3,3]))



