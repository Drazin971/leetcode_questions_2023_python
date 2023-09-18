class Solution:
  def minimizeMax(self, nums: list[int], p: int) -> int:

    if p == 0: return 0
    
    nums = sorted(nums)

    l, r = 0, 10**9

    def is_valid(level):
      i, count = 0, 0
      while i < len(nums) - 1:
        if abs(nums[i] - nums[i+1]) <= level:
          count +=1 
          i += 2
          if count == p:
            return True
        else:
          i += 1
      return False
      

    while l <= r:
      m = (l + r) // 2
      if is_valid(m):
        r = m -1
        sol = m
      else:
        l = m +1
  
    return sol

sol = Solution()

print(sol.minimizeMax(nums = [10,1,2,7,1,3], p = 2)) #1

print(sol.minimizeMax(nums = [4,2,1,2], p = 1)) #0

print(sol.minimizeMax(nums = [2,6,2,4,2,2,0,2], p = 4)) #2
