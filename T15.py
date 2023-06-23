class Solution:
  def threeSum(self, nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    triples = []

    for i in range(len(nums)):
      if i>0 and nums[i]==nums[i-1]:
        continue
      j, k = i+1, len(nums)-1
      while j < k:
        suma = nums[i]+nums[j]+nums[k]
        if suma==0:
          triples.append([nums[i],nums[j],nums[k]])
          j+=1
          while nums[j-1]==nums[j] and j<k: j+=1 
        elif suma>0:
          k-=1
        elif suma<0:
          j+=1

   
    return triples
    


      
    
     
sol=Solution()

print(sol.threeSum(nums = [-1,0,1,2,-1,-4])) #Output: [[-1,-1,2],[-1,0,1]]
print(sol.threeSum([0,1,1])) #[]
print(sol.threeSum([0,0,0])) #Output: [[0,0,0]]
print(sol.threeSum([0,0,0,0]))

      
