class Solution:
    def isHappy(self, n: int) -> bool:
      helper=0
      if n<10 and n!=7 and n!=1:
        return False
      while n > 0:
        helper += (n % 10) ** 2
        n = n // 10
        print(helper, n)
      if helper == 1:
        return True
      else:
        return self.isHappy(helper)
        
      
          
     

sol = Solution()

print(sol.isHappy(n =8))
