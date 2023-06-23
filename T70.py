class Solution:
    def climbStairs(self, n: int) -> int:
     db = [0] * (n+1)
     db[0], db[1] = 1,1
     for i in range (2,n+1):
        db[i] = db[i-1] + db[i-2]
     return db[n]
          
          

        
sol = Solution()

print(sol.climbStairs(4))