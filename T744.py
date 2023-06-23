class Solution:
  def nextGreatestLetter(self, letters: list[str], target: str) -> str:
    n=len(letters)

    for i in range(n):
      if ord(letters[i]) > ord(target):
        return letters[i]
  
    return letters[0]
     
      

sol = Solution()

print(sol.nextGreatestLetter(letters = ["x","x","y","y"], target = "z"))