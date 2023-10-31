class Solution:
  def majorityElement(self, nums: list[int]) -> list[int]:
    freq = len(nums) / 3
    res = []

    for num in set(nums):
      if nums.count(num) > freq:
        res.append(num)

    return res
    

sol = Solution()

print(sol.majorityElement(nums = [3,2,3]))  # 3