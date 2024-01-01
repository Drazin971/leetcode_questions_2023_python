class Solution:

  def checkArithmeticSubarrays(self, nums: list[int], l: list[int],
                               r: list[int]) -> list[bool]:

    def is_aritmetic(sq: list[int]) -> bool:
      d = sq[1] - sq[0]
      for i in range(1, len(sq)):
        if sq[i] - sq[i - 1] != d: return False
      return True

    res = []

    for i in range(len(l)):
      seq = sorted(nums[l[i]:r[i] + 1])
      res.append(is_aritmetic(seq))

    return res


sol = Solution()

print(
  sol.checkArithmeticSubarrays(nums=[4, 6, 5, 9, 3, 7],
                               l=[0, 0, 2],
                               r=[2, 3, 5]))  # [true,false,true]
