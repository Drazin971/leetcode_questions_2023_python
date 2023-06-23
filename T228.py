class Solution:
  def summaryRanges(self, nums: list[int]) -> list[str]:
    ranges = []
    if len(nums)==0:
      return None
    start_of_range = nums[0]
    i=1
    nums.append(float('inf'))
    while i < len(nums):
      if nums[i] == nums[i-1]+1:
        i+=1
        continue
      if nums[i] > nums[i-1]+1:
        if start_of_range == nums[i-1]:
          ranges.append(str(nums[i-1]))
        else:
          ranges.append(str(start_of_range)+"->"+str(nums[i-1]))
        start_of_range = nums[i]
        i+=1
          
    return ranges
        
      


sol=Solution()

print(sol.summaryRanges(nums = [0,2,3,4,6,8,9]))
print(sol.summaryRanges(nums = [0]))
