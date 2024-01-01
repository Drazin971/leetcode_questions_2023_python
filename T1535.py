class Solution:
  def getWinner(self, arr: list[int], k: int) -> int:
    win_count = 0 

    while True:
      if len(arr) < 2:
        return arr[0]
      if arr[0] < arr[1]:
        arr.pop(0)
        win_count = 1
      else:
        arr.pop(1)
        win_count += 1
      if win_count == k:
        return arr[0]



sol=Solution()

print(sol.getWinner(arr = [2,1,3,5,4,6,7], k = 2)) #Output: [[-1,-1,2],[-1,0,1]]