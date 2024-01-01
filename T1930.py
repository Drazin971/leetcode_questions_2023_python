class Solution:
  def countPalindromicSubsequence(self, s: str) -> int:
    l = set(s)
    res = 0

    for i in l:
      first = s.find(i)
      last = s.rfind(i)
      res += len(set(s[first+1:last]))

    return res

class Solution:
  def countPalindromicSubsequence(self, s: str) -> int:
    l = set()
    res = set()

    for i in range(len(s)):
      for letter in l:
        if letter in s[i+1:]:
          res.add(letter + s[i] + letter)
      l.add(s[i])

    return len(res)

sol=Solution()

print(sol.countPalindromicSubsequence(s = "bbcbaba")) #4 