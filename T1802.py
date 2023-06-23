class Solution:
  def maxValue(self, n: int, index: int, maxSum: int) -> int:  
    nums = [1] * n

    checked_range=0
    while sum(nums)<=(maxSum-min(checked_range,n)):
      nums[index]+=1
      for i in range(max(0,index-checked_range),min(len(nums),index+checked_range+1)):
        if abs(nums[i]-nums[index])>1:
          nums[i]+=1
        print(nums)
      checked_range+=1

    if sum(nums)>maxSum:
      nums[index]-=1
    return(nums[index])

sol = Solution()

print(sol.maxValue(n = 4, index = 0,  maxSum = 4)) #1
print(sol.maxValue(n = 6, index = 1,  maxSum = 10)) #3
print(sol.maxValue(n = 3, index = 2,  maxSum = 18)) #7
print(sol.maxValue(n = 8, index = 7,  maxSum = 14)) #4
print(sol.maxValue(n = 7, index = 5,  maxSum = 30)) #6
print(sol.maxValue(n = 4, index = 2,  maxSum = 6)) #2
#print(sol.maxValue(n = 9, index = 0,  maxSum = 90924720)) #2