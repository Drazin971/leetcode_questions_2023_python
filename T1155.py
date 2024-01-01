MOD = 10**9 + 7


class Solution:

  def numRollsToTarget(self, n: int, k: int, target: int) -> int:
    cache = {}

    def count(n, target):
      if n == 0:
        return 1 if target == 0 else 0
      if (n, target) in cache:
        return cache[(n, target)]
      res = 0
      for i in range(1, k + 1):
        res = (res + count(n - 1, target - i)) % MOD
      cache[(n, target)] = res
      return res

    return count(n, target)


sol = Solution()

print(sol.numRollsToTarget(n=2, k=6, target=7))  # 6
