class Solution:
  def wordPattern(self, pattern: str, s: str) -> bool:
   words = list(s.split())
   check = {}

   if len(words) != len(pattern): return False

   for i in range(len(pattern)):
     if pattern[i] not in check:
       if words[i] not in check.values():
        check[pattern[i]]=words[i]
       else: return False
     elif check[pattern[i]] != words[i]:
       return False
 
   return True
      
    
    
     
    
sol=Solution()

print(sol.wordPattern(pattern = "abba", s = "dog cat cat dog")) #1

print(sol.wordPattern(pattern = "abba", s = "dog cat cat fish")) #0

print(sol.wordPattern(pattern = "aaaa", s = "dog cat cat dog")) #0

print(sol.wordPattern(pattern = "abba", s = "dog dog dog dog")) #0

