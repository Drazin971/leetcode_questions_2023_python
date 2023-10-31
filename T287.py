class Solution:
  def findDuplicate(self, nums: list[int]) -> int:
    nums_sum = sum(nums)
    n= len(nums)
    ar_sum = n / 2 *(2 * (n-1))

    diff = nums_sum - ar_sum

    return diff


sol = Solution()

print(sol.findDuplicate(nums = [3,1,3,4,2]))