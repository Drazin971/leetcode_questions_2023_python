class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
      for i in nums:
        if nums.count(i) > 1:
          return True
      return False

    
    
          
     

sol = Solution()

print(sol.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))
#104

