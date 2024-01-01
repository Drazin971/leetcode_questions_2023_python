class Solution:
  def minPairSum(self, nums: list[int]) -> int:
    nums.sort()
    min_pair = float("-inf")

    for i in range(len(nums)//2):
      min_pair = max(min_pair, nums[i] + nums[len(nums) - i - 1])

    return min_pair

sol=Solution()

print(sol.minPairSum(nums = [3,5,4,2,4,6])) # 2