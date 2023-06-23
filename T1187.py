class Solution:
  def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
    if len(arr1)<2: return 0
    
    arr2.sort()
    moves=0
    i=1
    
    while i<len(arr1):
      while arr1[i]<=arr1[i-1]:
        arr1[i-1]=arr2.pop(0)
        moves+=1
        if i>1: i-=1
      i+=1
      print(arr1, arr2)
    
    return moves 
    
     
sol=Solution()

print(sol.makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [1,3,2,4])) #1
print(sol.makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [4,3,1])) #2
print(sol.makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [1,6,3,3])) #-1
      