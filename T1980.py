class Solution:
  def findDifferentBinaryString(self, nums: list[str]) -> str:
    str_sum = {s for s in nums}

    def bt(i, cur):
      if i == len(nums):
        res = "".join(cur)
        return None if res in str_sum else res

      res = bt(i+1, cur)
      if res: return res

      cur[i] = "1"
      res = bt(i+1, cur)
      if res: return res


    return bt(0, ["0" for s in nums])

sol=Solution()

print(sol.findDifferentBinaryString(nums = ["111","011","001"])) # 2