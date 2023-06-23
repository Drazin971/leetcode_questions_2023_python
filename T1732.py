class Solution:
  def largestAltitude(self, gain: list[int]) -> int:
    alt,max_alt = 0, 0 
    for i in range(len(gain)):
      alt+=gain[i]
      max_alt=max(alt, max_alt)

    return max_alt
    
sol=Solution()

print(sol.largestAltitude(gain = [-5,1,5,0,-7])) #1
print(sol.largestAltitude(gain = [-4,-3,-2,-1,4,3,2])) #0