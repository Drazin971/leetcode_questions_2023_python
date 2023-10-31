class Solution:
  def numWays(self, steps: int, arrLen: int) -> int:
    MOD = 10**9 + 7
    dp = {}

    def find_way(pos = 0, step = steps):
      if pos == step == 0:
        return 1
      if (pos > step) or not (0 <= pos < arrLen):
          return 0
      if (pos,step) in dp:
        return dp[(pos,step)]

      dp[(pos, step)] = (find_way(pos + 1, step - 1) + find_way(pos, step - 1) + find_way(pos - 1, step - 1)) % MOD
      return dp[(pos,step)]

    return find_way()

sol = Solution()

print(sol.numWays(steps = 4, arrLen = 3))  # 4