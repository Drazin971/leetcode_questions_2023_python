class Solution:
  def maxFrequency(self, nums: list[int], k: int) -> int:
    nums.sort()
    l, r = 0, 0
    res, total = 0

    while r < len(nums):
        total += nums[r]

        while nums[r] * (r-l+1) > total + k:
            total -= nums[l]
            l+=1

        res = max(res,r-l+1)
        r+=1

    return res






sol=Solution()

print(sol.maxFrequency(nums = [1,4,8,13], k = 5)) # 2