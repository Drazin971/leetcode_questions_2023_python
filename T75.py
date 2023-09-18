class Solution:
  def sortColors(self, nums: list[int]) -> None:
    left, right = 0, len(nums) - 1

    for i in range(len(nums)):
      if nums[i] == 0:
        temp=nums[left]
        nums[left]=nums[i]
        nums[i]=temp
        left +=1
      elif nums[i] == 2:
        temp=nums[right]
        nums[right]=nums[i]
        nums[i]=temp
        right -=1
        
    return nums

sol = Solution()

print(sol.numMusicPlaylists(nums = [2,0,2,1,1,0])) #6

