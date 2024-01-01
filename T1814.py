MOD = 10**9 + 7
class Solution:
  def countNicePairs(self, nums: list[int]) -> int:

    res = {}

    def rev(n: int):
      rev_n = n % 10
      while n > 9:
        n = n // 10
        rev_n *= 10 
        rev_n += n % 10

      return rev_n

    for i in range(len(nums)):
      if nums[i] - rev(nums[i]) not in res:
        res[nums[i] - rev(nums[i])] = 1
      else:
        res[nums[i] - rev(nums[i])] += 1

    return (sum(n * (n-1) // 2 for n in res.values()) % MOD)

sol=Solution()

print(sol.countNicePairs(nums = [13,10,35,24,76])) # 4