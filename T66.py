class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
      carry=0
      for i in range(len(digits)-1,-1,-1):
        if i==len(digits)-1:
          digits[i]+=1
        if digits[i]+carry == 10:
          digits[i]=0
          carry=1
        elif carry==1:
          digits[i]+=1
          carry=0

      if carry==1:
        digits[0]=0
        digits.insert(0,1)
      return digits  
        
sol = Solution()

print(sol.plusOne([9,9,9,9]))