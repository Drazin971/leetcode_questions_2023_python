class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    pointer = 0
    for letter in s:
      print(letter,pointer, t)
      if letter not in t[pointer:]:
        return False
      else:
        pointer = t.index(letter,pointer) 
        pointer +=1
    return True
      
    
      

sol=Solution()

print(sol.isSubsequence(s = "abc", t = "ahbgdc")) #tru
print(sol.isSubsequence(s = "axc", t = "ahbgdc")) #false
print(sol.isSubsequence(s = "aaaaa",t = "bbaaa")) #false
print(sol.isSubsequence(s = "twn",t = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn")) #tru
