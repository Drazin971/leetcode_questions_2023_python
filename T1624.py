class Solution:
  def maxLengthBetweenEqualCharacters(self, s: str) -> int:
      chars = {}
      dupl = False
      for i, ch in enumerate(s):
          if ch not in chars:
            chars[ch] = (i, 0)
          else:
            dupl = True
            chars[ch] = (chars[ch][0], i - chars[ch][0] - 1)
      score = max(e-s for s, e in chars.values())
      return score if dupl else -1

sol=Solution()

print(sol.maxLengthBetweenEqualCharacters("scayofdzca")) # 6

print(sol.maxLengthBetweenEqualCharacters(s = "cbzxy")) # 2