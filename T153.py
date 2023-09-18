class Solution:
  def findMin(self, nums: list[int]) -> int:
    lo, hi = 0, len(nums)-1
    ans=float('inf')

    while lo<=hi:
     mid = lo + (hi-lo) // 2
     
     if nums[lo] <= nums[mid]:
       ans = min(ans, nums[lo])
       lo = mid + 1 
     else:
       ans = min(ans, nums[mid])
       hi = mid - 1
       
    return ans
      



sol=Solution()

r=sol.findMin(nums = [4,5,6,7,0,1,2]) # [0]

print(r)

r=sol.findMin(nums = [3,4,1,2]) # [1]

print(r)