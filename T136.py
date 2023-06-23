class Solution:
    def singleNumber(self, nums: list[int]) -> int:
      for i in range(len(nums)):
        temp = nums[i]
        nums[i]=None
        if temp not in nums:
          return temp
        nums[i]=temp
      
        

sol = Solution()

print(sol.singleNumber([2,2,1]))
