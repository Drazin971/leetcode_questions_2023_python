class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
      m = 1
      alice, john = 0, 0
      while len(piles)>0:
        find_opt = self.optimumX(piles, m)
        print("find opt", find_opt)
        for i in range(find_opt):
          alice += piles[0]
          m += 1
          piles.pop(0)
          print("Alice", alice)
        find_opt = self.optimumX(piles, m)
        print("find opt", find_opt)
        for i in range(find_opt):
          john += piles[0]
          m += 1
          piles.pop(0)
          print("John", john)
      
    def optimumX(self, piles: list[int], currentMax: int) -> int:
      if len(piles)<=currentMax:
        return(len(piles))
      for i in range(1,currentMax*2):
         return max(self.optimumX(piles[i:],i*2))
      

    
    
          
     

sol = Solution()

print(sol.stoneGameII([1,2,3,4,5,100]))
#104


