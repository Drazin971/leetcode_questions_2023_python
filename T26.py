class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
      pointer = 0
      cur = -999
      for i in range(len(nums)):
        if nums[i] > cur:
          nums[pointer] = nums[i]
          pointer +=1
          cur = nums[i]

      return pointer

sol = Solution()

print(sol.removeDuplicates([1,2,3,4,4,4,5]))
