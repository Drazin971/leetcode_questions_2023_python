class Solution:
  def sortArrayByParity(self, nums: list[int]) -> list[int]:
    l, r = 0, len(nums) - 1
    while l < r:
      if nums[l] % 2 == 1:
        while l < r and nums[r] % 2 == 1:
          r -= 1
        temp = nums[r]
        nums[r] = nums[l]
        nums[l] = temp
        l += 1
        r -= 1
      else:
        l += 1

    return nums