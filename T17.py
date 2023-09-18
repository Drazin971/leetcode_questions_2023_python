class Solution:
  def letterCombinations(self, digits: str) -> list[str]:
    combinations = []
    phone_keys = {
      '2': 'abc',
      '3': 'def',
      '4': 'ghi',
      '5': 'jkl',
      '6': 'mno',
      '7': 'pqrs',
      '8': 'tuv',
      '9': 'wxyz'}

    if not digits:
      return []
    
    def btrack(curr: str,i:int):
      if len(curr)==len(digits):
        combinations.append(curr)
        return
      for letter in phone_keys[digits[i]]:
        btrack(curr+letter,i+1)

    btrack("",0)
        
    return combinations
                     
sol = Solution()

r=sol.letterCombinations(digits = "23") #["ad","ae","af","bd","be","bf","cd","ce","cf"]

print(r)

r=sol.letterCombinations(digits = "2") #["a","b","c"]

print(r)