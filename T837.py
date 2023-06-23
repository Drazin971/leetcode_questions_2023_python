class Solution:
  def new21Game(self, n: int, k: int, maxPts: int) -> float:

    counter = 0
    cases =0 
    
    if k-maxPts < 0:
      start = 0 
    else:
      start = k-maxPts
    
    for i in range(start,k):
      for j in range(1,maxPts+1):
        if (i+j >=k):
          cases +=1
          if (i+j <= n):
            counter += 1 
            print(i + j, counter, cases)

    
    return counter/cases
          
     

sol = Solution()

print(sol.new21Game(n = 21, k =17, maxPts = 10))
