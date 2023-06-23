class Solution:
    def majorityElement(self, nums: list[int]) -> int:
      lista = {}
      lista[0]=0
      i=0
      while max(lista.values())<len(nums)//2+1:
        if nums[i] in lista.keys():
          lista[nums[i]] +=1
        else:
          lista[nums[i]]=1
        i+=1
        
      return max(lista, key=lista.get)


sol = Solution()

print(sol.majorityElement([2,2,1,1,1,2,2]))


        