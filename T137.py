class Solution:
  def singleNumber(self, nums: list[int]) -> int:
     list_of_nums = {}
     for num in nums:
       if num not in list_of_nums.keys():
         list_of_nums[num]=1
       else:
         list_of_nums[num]+=1

     for key, val in list_of_nums.items():
        if val==1:
          return key
        
               
         
      

sol=Solution()

print(sol.singleNumber([0,1,0,1,0,1,99])) 












 



