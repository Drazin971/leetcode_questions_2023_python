class Solution:
  def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
    arr.sort()

    arr[0] = 1

    for i in range(1,len(arr)):
      arr[i] = min(i + 1, arr[i], arr[i-1] + 1)

    return arr[-1]
      

sol=Solution()

print(sol.maximumElementAfterDecrementingAndRearranging(arr = [2,2,1,2,1])) # 2