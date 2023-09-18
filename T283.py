class Solution:
  def moveZeroes(self, nums: list[int]) -> None:

    for i in range(len(nums)):
      nums.append(0)
      nums.remove(0)
      
    return nums  
    

sol=Solution()

print(sol.moveZeroes(nums = [0,1,0,18,12])) #[1,3,12,0,0]
