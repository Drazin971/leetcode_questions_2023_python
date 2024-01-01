MOD = 10**9 + 7

class Solution:
  def numberOfWays(self, corridor: str) -> int:
    seats = []

    for i, s in enumerate(corridor):
      if corridor[i] == "S": seats.append(i)

    l = len(seats)

    if l < 2 or l % 2 == 1: return 0

    res, i = 1, 1

    while i < l - 1:
        res = res * (seats[i+1] - seats[i]) % MOD
        i += 2

    return res

sol=Solution()

print(sol.numberOfWays(corridor = "SSPPSPS")) # 3
