class Solution:
  def reductionOperations(self, nums:list[int]) -> int:

    nums.sort(reverse=True)
    total = 0

    for i in range(1,len(nums)):
      if nums[i-1] > nums[i]:
        total = total + i

    return total   

sol=Solution()

print(sol.reductionOperations(nums = [4,1,1,2,2,3])) # 4


print(sol.reductionOperations(nums = [7,9,10,8,6,4,1,5,2,3])) # 45