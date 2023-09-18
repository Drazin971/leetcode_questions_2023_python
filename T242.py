class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

      if len(s) != len(t): return False
        
      for i in range(len(s)):
        t=t.replace(s[i],"*",1)

      return True if t.count("*")==len(t) else False
    
    
     
    
sol=Solution()

print(sol.isAnagram(s = "anagram", t = "nagaram")) #1

print(sol.isAnagram(s = "rat", t = "car")) #0

print(sol.isAnagram(s = "aacc", t = "ccac")) #0
