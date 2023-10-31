class Solution:
  def sortByBits(self, arr: list[int]) -> list[int]:
    def bit_count(num):
      return num // 2 + num % 2
      
    return arr.sort(key = bit_count)

sol = Solution()

print(sol.sortByBits([0,1,2,3,4,5,6,7,8])  # 1