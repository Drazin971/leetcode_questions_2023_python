class Solution:
  def combinationSum4(self, nums: list[int], target: int) -> int:

    def dfs(c, result):
      if c == target:
        return 1
      if c > target:
        return 0
      for num in nums:
        result += dfs(c+num) 
      return result
        
    return dfs(0,0)

sol = Solution()

print(sol.combinationSum4(nums = [1,2,3], target = 4)) #7

print(sol.combinationSum4(nums = [9], target = 3)) #0