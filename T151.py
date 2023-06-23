class Solution:
  def reverseWords(self, s: str) -> str:
    new_s = s.rsplit(sep=" ")
    while "" in new_s:
      new_s.remove("")
    s=""
    for word in new_s:
      s=word + " " + s
    return s[:-1]
      
    
  

sol=Solution()

print(sol.reverseWords(s = "a good   example")) #"example good a"