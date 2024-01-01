class Solution:

  def maxCoins(self, piles: list[int]) -> int:
    piles.sort(reverse=True)
    start, end = 0, len(piles) - 1
    res = 0

    while start < end:
      res += piles[start + 1]
      start += 2
      end -= 1

    return res


sol = Solution()

print(sol.maxCoins(piles=[2, 4, 1, 2, 7, 8]))  # 9
