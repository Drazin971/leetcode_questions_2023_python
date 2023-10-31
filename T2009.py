class Solution:
    def minOperations(self, nums: list[int]) -> int:
      res = len(nums) - len(set(nums))
      return res

sol = Solution()

print(sol.minOperations(nums = [1,1,2,3,5,6]))  # 2
        