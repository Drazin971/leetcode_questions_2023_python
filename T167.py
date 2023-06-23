class Solution:
  def twoSum(self, numbers: list[int], target: int) -> list[int]:
    for number in numbers:
      if target-number in numbers:
        return [numbers.index(number)+1,numbers.index(target-number,numbers.index(number)+1)+1]
    
     
sol=Solution()

print(sol.twoSum(numbers = [2,7,11,15], target = 9)) #[1,2]
print(sol.twoSum(numbers = [2,1,11,2], target = 4)) #[1,2]
