MOD = 10**9 + 7
from itertools import groupby

class Solution:
  def countHomogenous(self, s: str) -> int:

    return sum(
            x * (x + 1) >> 1
            for _, grp in groupby(s)
            for x in [len(list(grp))]
        ) % MOD 

# n* (n+1) / 2

sol=Solution()

print(sol.countHomogenous("abbcccaa")) #4 