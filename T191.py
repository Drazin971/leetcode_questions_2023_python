class Solution:
    def hammingWeight(self, n: int) -> int:
      return bin(n)[2:].count("1")

    

          
     

sol = Solution()

print(sol.hammingWeight(1982))
#104
