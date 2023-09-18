class Solution:
  def searchRange(self, nums: list[int], target: int) -> list[int]:
    lo, hi = 0, len(nums)-1

    def find_start_end(targeted: int):
      targeted_start = targeted_end = targeted
      while targeted_start>=0 and nums[targeted_start]==target:
        targeted_start-=1
      while targeted_end<=len(nums)-1 and nums[targeted_end]==target:
        targeted_end+=1

      return [targeted_start+1, targeted_end-1] 
    
    while lo<=hi:
     mid = lo + (hi-lo) // 2
     if nums[mid] == target: return find_start_end(mid)
     if nums[mid] <= target:
       lo = mid + 1
     else:
       hi = mid-1
       
    return [-1,-1]  
     
      



sol=Solution()

r=sol.searchRange(nums = [5,7,7,8,8,10], target = 8) # [3,4]

print(r)

r=sol.searchRange(nums = [5,7,7,8,10,10], target = 7) # [-1,-1]

print(r)

r=sol.searchRange(nums = [], target = 0) # [-1,-1]

print(r)
