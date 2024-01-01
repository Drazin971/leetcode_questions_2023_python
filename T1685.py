import numpy as np


class Solution:

  def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
    l_nums = len(nums)
    sum_l = 0
    sum_r = np.sum(nums)
    res = []

    for i in range(l_nums):
      num = sum_r - nums[i] * (l_nums - i) + nums[i] * i - sum_l
      res.append(int(num))
      sum_l += nums[i]
      sum_r -= nums[i]

    return res


sol = Solution()

print(sol.getSumAbsoluteDifferences(nums=[1, 4, 6, 8, 10]))  # [24,15,13,15,21]
