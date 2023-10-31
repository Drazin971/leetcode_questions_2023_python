class Solution:
  def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

    def fib_sum(n):
      a, b = 0, 1
      total_sum = 0
      for _ in range(n+2):
        total_sum += a
        a, b = b, a + b
      return total_sum
      
    def fib(n):
      if n==0:
        return 1
      if n==1:
        return 2
      return fib(n-1) + fib (n-2)
                 
    rest = fib_sum(query_row)

    print(rest)

   

sol = Solution()

print(sol.champagneTower(poured = 100000009, query_row = 33, query_glass = 17)) #1

print(sol.champagneTower(poured = 2, query_row = 1, query_glass = 1)) #2
