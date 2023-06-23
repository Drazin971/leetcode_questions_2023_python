class Solution:
  def getAverages(self, nums: list[int], k: int) -> list[int]:
    list_of_averages = []

    sum_of_range=0
     
    for i in range(len(nums)):
      #print(list_of_averages,k,i)
      if (i<k or i>len(nums)-k-1):
        list_of_averages.append(-1)
      else:
        if sum_of_range==0:
          for j in range(i-k,i+k+1):
            sum_of_range += nums[j] 
        else:
          sum_of_range = sum_of_range - nums[i-k-1] + nums[i+k]
        avg = sum_of_range // (2*k+1)
        list_of_averages.append(avg)
    return list_of_averages  
    
sol=Solution()

print(sol.getAverages(nums = [7,4,3,9,1,8,5,2,6], k = 3)) #[-1,-1,-1,5,4,4,-1,-1,-1]

print(sol.getAverages(nums = [10000], k = 0)) #[10000]

print(sol.getAverages(nums = [10000], k = 8)) #[-1]]