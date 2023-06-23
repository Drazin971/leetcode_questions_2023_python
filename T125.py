class Solution:
    def isPalindrome(self, s: str) -> bool:
      oldS = s.strip().lower()
      s = ""
      for i in range(len(oldS)):
        if oldS[i].isalnum():
          s = s + oldS[i]
      print(s)
      i=0
      while s and i<=(len(s)//2):
        if s[i] is not s[len(s)-i-1]:
          return False
        i+=1

      return True
      
        

sol = Solution()

print(sol.isPalindrome("0P"))
