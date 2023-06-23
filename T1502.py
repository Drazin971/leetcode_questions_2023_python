class Solution:
  def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
    arr.sort()
    if len(arr)>1:
      dist = arr[1] - arr[0]
      for i in range(1,len(arr)):
        if arr[i] - arr[i-1] != dist:
          return False
    return True


sol = Solution()

print(sol.canMakeArithmeticProgression([3,5,1]))