class Solution:
  def candy(self, ratings: list[int]) -> int:
    n = len(ratings)
    candies = [1 for i in range(n)]

    for i in range(1,n):
      if ratings[i-1] < ratings[i]:
        candies[i] = candies[i-1] + 1

    for i in range(n-2,-1,-1):
      if ratings[i] > ratings[i+1]:
          candies[i] = max(candies[i],candies[i+1] + 1)

    #print(candies)
    
    return sum(candies)
      

sol = Solution() 

print(sol.candy(ratings = [1,0,2])) #5

print(sol.candy(ratings = [1,2,2])) #4

print(sol.candy(ratings = [1,3,2,2,1])) #7