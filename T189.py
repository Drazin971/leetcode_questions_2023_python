class Solution:
  def rotate(self, nums: list[int], k: int) -> None:
    for i in range(k):
      nums.insert(0,nums.pop(len(nums)-1))
    print(nums)

sol = Solution()

print(sol.rotate(nums = [1,2,3,4,5,6,7], k = 3))