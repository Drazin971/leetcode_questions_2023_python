class Solution:
  def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
    flowers.sort()
    flower_end = sorted(flowers(key=lambda x: x[1]))

    print(flowers)
    print(flower_end)

sol = Solution()

print(sol.fullBloomFlowers(flowers = [[1,10],[3,3]], poeple = [3,3,2]))  # [2,2,1]