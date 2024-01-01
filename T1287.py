class Solution:
  def findSpecialInteger(self, arr: list[int]) -> int:
      arr.sort(key = lambda x: arr.count(x))
      print(arr)
      return arr[0]

sol=Solution()

print(sol.findSpecialInteger(arr = [1,2,2,6,6,6,6,7,10])) # 13