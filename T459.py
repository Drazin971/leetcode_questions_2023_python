class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

      for i in range(1,(len(s) // 2) + 1):
        substring = s[:i]
        new_string = "" + substring * (len(s) // i)
        if  new_string == s:
          return True
      return False  
    

sol = Solution()

print(sol.repeatedSubstringPattern(s = "abab")) # True

print(sol.repeatedSubstringPattern(s = "aba")) #False

print(sol.repeatedSubstringPattern(s = "abcabcabcabc")) # True
