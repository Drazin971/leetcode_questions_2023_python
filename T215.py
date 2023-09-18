import heapq

class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
      return heapq.nlargest(k, nums)[-1]
    

sol=Solution()

r=sol.findKthLargest(nums = [3,2,1,5,6,4], k = 2) # 5

print(r)

r=sol.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4) # 4

print(r)