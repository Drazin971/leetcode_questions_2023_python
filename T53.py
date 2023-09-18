class Solution:
  def maxSubArray(self, nums: list[int]) -> int:
    cur=0
    max_sum=nums[0]

    for n in nums:
      if cur<0:
        cur=0
      cur+=n
      max_sum=max(max_sum,cur)
      
    return max_sum                      

sol=Solution()

r=sol.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]) #6

print(r)