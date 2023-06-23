class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
      while val in nums:
        nums.remove(val)

      return len(nums)
      
sol = Solution()

print(sol.removeElement([0,1,2,2,3,0,4,2],2))
