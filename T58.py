class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      l1 = s.rsplit()
      return len(l1[len(l1)-1])
        
sol = Solution()

print(sol.lengthOfLastWord("   fly me   to   the moon  "))

