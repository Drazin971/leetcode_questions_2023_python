class Solution:
  def rob(self, nums: list[int]) -> int:
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums[0], nums[1])
    
    sol = [0] * len(nums)

    sol[0]=nums[0]
    sol[1]=max(nums[0],nums[1])

    for n in range(2, len(nums)):
      sol[n]=max(sol[n-1], sol[n-2] + nums[n])
    
    return sol[-1]

sol=Solution()

print(sol.rob(nums = [1,2,3,1])) #4

print(sol.rob(nums = [2,7,9,3,1])) #12
