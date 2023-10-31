class Solution:
  def longestStrChain(self, words: list[str]) -> int:
    words.sort(key=len)

    dp = {}
    res = 0

    for word in words:
      dp[word] = 1
      for i in range(len(word)):
        prev = word[:i] + word[i+1:]
        if prev in dp:
          dp[word] = max(dp[word], dp[prev] + 1)
      res = max(res, dp[word])  
    
    return res

sol = Solution()

print(sol.longestStrChain(words = ["a","b","ba","bca","bda","bdca"])) #4

print(sol.longestStrChain(words = ["xbc","pcxbcf","xb","cxbc","pcxbc"])) #5

        