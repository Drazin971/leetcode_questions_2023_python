class Solution:
    def mySqrt(self, x: int) -> int:
      if x==0:
        return 0
      first = 0 
      last = x
          
      while first <= last:
        mid = first + (last - first) // 2
        if mid * mid == x:
          return mid
        elif mid * mid > x:
          last = mid - 1
        else:
          first = mid + 1
        
      return last
        
sol = Solution()

print(sol.mySqrt(5))