class Solution:
  def rangeBitwiseAnd(self, left: int, right: int) -> int:

    res = 0
      
    while left < right:

      left >>= 1
      right >>= 1
      res += 1

    return left << res

sol=Solution()

#print(sol.rangeBitwiseAnd(left = 5, right = 7)) #4

print(sol.rangeBitwiseAnd(left = 1, right = 1)) #0

print(sol.rangeBitwiseAnd(left = 1, right = 2147483647)) #0
