class Solution:
  def findPeakElement(self, nums: list[int]) -> int:
    prev = float('-inf')
    for i in range(len(nums)):
      if nums[i]>=prev:
        prev=nums[i]
      else:
        return i-1
    return len(nums)-1

sol=Solution()

r=sol.findPeakElement(nums = [1,2,3,1]) #2

print(r)

r=sol.findPeakElement(nums = [1,2,3,4,5,6,7]) #5

print(r)