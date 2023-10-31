class Solution:
  def numIdenticalPairs(self, nums: list[int]) -> int:
    res = 0
    
    for number in set(nums):
      current_count = nums.count(number) 
      res += current_count * (current_count-1) // 2

    return res

sol = Solution()

print(sol.winnerOfGame(nums = [1,2,3,1,1,3]))  # 4