class Solution:
  def backspaceCompare(self, s: str, t: str) -> bool:

    s_mod, t_mod = "", ""
    
    for i in range(len(s)):
      if s[i] != "#":
        s_mod += s[i]
      else:
        s_mod = s_mod[:-1]

    for j in range(len(t)):
      if t[j] != "#":
        t_mod += t[j]
      else:
        t_mod = t_mod[:-1]
      
    return s == t
    
    

sol = Solution()

print(sol.getRow(s = "ab##", t = "c#d#"))  # [1,3,3,1]