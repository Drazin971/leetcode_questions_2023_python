class Solution:
  def minExtraChar(self, s: str, dictionary: list[str]) -> int:
    max_extra_chars = len(s)+1
    dp = [max_extra_chars] * (len(s) + 1)
    dp[0] = 0

    for i in range(1,len(s)+1):
      dp[i] = dp[i-1] + 1
      
      for j in range(1,i+1):
        new_string = s[i-j:i]
        if new_string in dictionary:
          dp[i] = min(dp[i], dp[i-j])

    return dp[-1]
          
      

sol = Solution()

print(sol.minExtraChar(s = "leetscode", dictionary = ["leet","code","leetcode"])) #1

print(sol.minExtraChar(s = "sayhelloworld", dictionary = ["hello","world"])) #3
        