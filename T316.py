class Solution:
  def removeDuplicateLetters(self, s: str) -> str:
    fl = ord("a")
    found = set()

    for i in range(fl, fl+26):
      if str(i) not in found:
        found.add(chr(i))
      
    found.sort()

    return str(found)
    

sol = Solution()

print(sol.removeDuplicateLetters(s = "bcabc")) #1

