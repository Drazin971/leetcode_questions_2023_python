class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    dict = {}

    for pos in range(len(s)):
      if s[pos] not in dict:
        if t[pos] not in dict.values():
          dict[s[pos]] = t[pos]
        else: return False
      elif t[pos] != dict[s[pos]]:
        return False
         
    return True
    
    
    
     
    
sol=Solution()

print(sol.isIsomorphic(s = "egg", t = "add")) #1

print(sol.isIsomorphic(s = "foo", t = "bar")) #0

print(sol.isIsomorphic(s = "paper", t = "title")) #1

print(sol.isIsomorphic(s = "bbbaaaba", t = "aaabbbba")) #0

print(sol.isIsomorphic(s = "badc", t = "baba")) #0

        
    
    
     
    
sol=Solution()

print(sol.isIsomorphic(s = "egg", t = "add")) #1

print(sol.isIsomorphic(s = "foo", t = "bar")) #0

print(sol.isIsomorphic(s = "paper", t = "title")) #1

print(sol.isIsomorphic(s = "bbbaaaba", t = "aaabbbba")) #0
