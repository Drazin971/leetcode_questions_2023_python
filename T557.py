class Solution:
  def reverseWords(self, s: str) -> str:
    reversed_words = ""
    for word in s.strip():
      reversed_words += reversed(word)
    return reversed_words
    
sol = Solution()

print(sol.find132pattern("Let's take LeetCode contest")) 

