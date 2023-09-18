from collections import defaultdict

class Solution:
  def reorganizeString(self, s: str) -> str:
    letters = defaultdict(0)
    for letter in s:
      letters[letter] += 1
  print(letters)
    

sol = Solution()

print(sol.reorganizeString(s = "aab")) #"aba"

print(sol.reorganizeString(s = "aaab")) #""