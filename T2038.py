class Solution:
  def winnerOfGame(self, colors: str) -> bool:
    ejs, bees = 0, 0
    for i in range(1,len(colors)-1):
      if colors[i-1] == colors[i] == colors[i+1] == "A":
        ejs += 1
      if colors[i-1] == colors[i] == colors[i+1] == "B":
        bees += 1
    return ejs > bees


sol = Solution()

print(sol.winnerOfGame(colors = "AAABABB")) #true

print(sol.winnerOfGame(colors = "AA")) #false

print(sol.winnerOfGame(colors = "ABBBBBBBAAA")) #true

