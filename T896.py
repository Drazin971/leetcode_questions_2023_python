class Solution:
  def isMonotonic(self, nums: list[int]) -> bool:
    is_decreasing, is_increasing = False

    if len(nums) == 1:
      return True

    for i in range(1,len(nums)):
      if nums[i] < nums[i-1]:
        is_decreasing = True
      if nums[i] > nums[i-1]:
        is_increasing = True
      if is_decreasing and is_increasing:
        return False

    return True
      
    


sol = Solution()

print(sol.isMonotonic(nums = [6,5,4,4])) 
        