class Solution:
  def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
      return max(max(left) if left else n - n, n - min(right) if right else 0)