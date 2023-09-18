form collections import defaultdict

class Solution:
  def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:

    dp = [0] * goal
    dp[0] = 1
    MOD = 10**9 + 7

    for i in range(1,goal):
      dp[i] = dp[i-1] * ()
      
      