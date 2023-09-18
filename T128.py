class Solution:
  def longestConsecutive(self, nums: list[int]) -> int:
    if len(nums)<2: return len(nums)
    nums = sorted(set(nums))
    streaks = []
    streak = 1
    for i in range(1,len(nums)):
      if nums[i]==nums[i-1]+1:
        streak +=1
      else:
        streaks.append(streak)
        streak = 1
    streaks.append(streak)
    return max(streaks)
      
      
    
sol=Solution()

print(sol.longestConsecutive(nums = [100,4,200,1,3,2])) #4

print(sol.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1])) #9












 



