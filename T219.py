class Solution:
  def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
    if len(nums) == len(set(nums)): return False
    for i in range(len(nums)):
      for j in range (max(i-k,0), min(i+k+1,len(nums))):
        #print(nums[i], nums[j], i, j)
        if (nums[i]==nums[j]) and (i != j):
          return True
    return False
    
sol=Solution()

print(sol.containsNearbyDuplicate(nums = [1,2,3,1], k = 3)) #1

print(sol.containsNearbyDuplicate(nums = [1,0,1,1], k = 1)) #1

print(sol.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)) #0