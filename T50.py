class Solution:
  def myPow(self, x: float, n: int) -> float:
    return x**n


sol=Solution()

r=sol.myPow(x = 2.00000, n = 10) #1024

print(r)

r=sol.myPow(x = 2.10000, n = 3) #9.26100

print(r)

r=sol.myPow(x = 2.00000, n = -2) #0.25

print(r)