class Solution:
  def maxSubarraySumCircular(self, nums: list[int]) -> int:      

    max_sum = min_sum = nums[0]
    total_sum = sum(nums)
    cur_sum, cur_min = 0, 0 
    
    for n in nums:
      if cur_sum<0:
        cur_sum = 0
      cur_sum+=n
      max_sum=max(max_sum,cur_sum)
      if cur_min>0:
        cur_min = 0
      cur_min+=n
      min_sum=min(min_sum, cur_min)

    if max_sum>0:
     return max(max_sum, total_sum-min_sum)
    else:
      return max_sum
      

sol=Solution()

r=sol.maxSubarraySumCircular(nums = [5,-3,5]) #10

print(r)