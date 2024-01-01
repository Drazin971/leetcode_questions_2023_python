class Solution:
  def maxScore(self, s: str) -> int:
    max_sc = 0
    zeroes, ones = 0, 0
  
    for i in range(len(s)):
      ones += int(s[i])

    for i in range(1, len(s)):
      if s[i-1] == "0":
        zeroes += 1
      else:
        ones -=1
      max_sc  = max(max_sc, zeroes + ones) 
    return max_sc

sol=Solution()

print(sol.maxScore(s = "011101"))