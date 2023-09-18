class Solution:
  def longestPalindrome(self, s: str) -> str:

    max_off = 0
    l_pali = ""

    for i in range(len(s)):
      l , r = i, i
      while r < len(s) and l >= 0 and s[l] == s[r]:
        
        if (r - l + 1) > max_off:
            max_off = r - l + 1
            l_pali = s[l : r + 1]
        
        r += 1
        l -=1

      l , r = i, i + 1
      while r < len(s) and l >= 0  and s[l] == s[r]:
        
        if (r - l + 1) > max_off:
            max_off = r - l + 1
            l_pali = s[l : r + 1]
        
        r += 1
        l -=1
        
    return l_pali

   
sol = Solution()

print(sol.longestPalindrome(s = "ccdbabd")) #"bab"

print(sol.longestPalindrome(s = "cbbd")) #"bb"