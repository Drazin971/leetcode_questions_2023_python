class Solution:
  def removeDuplicates(self, nums: list[int]) -> int:
    if len(nums)<3:
      return len(nums)
    
    total=len(nums)
        
    for i in range(len(nums)-1,1,-1):
      if nums[i]==nums[i-1]==nums[i-2]:
        nums.pop(i)
        total-=1
      
        
            

    print(nums)
    return total 

sol = Solution()

print(sol.removeDuplicates(nums = [0,0,1,1,1,1,2,3,3]))