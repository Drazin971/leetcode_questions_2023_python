class Solution:
  def findArray(self, pref: list[int]) -> list[int]:
    n = len(pref)
    arr = [0 for _ in range(n)]
    arr[0] = pref[0]

    for i in range(1,n):
      arr[i] = pref[i-1] ^ pref[i]

    return arr 

sol = Solution()

print(sol.findArray(pref = [5,2,0,3,1]))  # [5,7,2,3,2]